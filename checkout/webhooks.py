from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .webhook_handler import StripeWH_Handler
import stripe
import json

@require_POST
@csrf_exempt
def webhook(request):
    """Listens for webhooks from Stripe """
    wh_secret = settings.STRIPE_WH_SECRET
    stripe_api_key = settings.STRIPE_SECRET_KEY

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(status=400, content=e)

    handler = StripeWH_Handler(request)     

    # Map webhook events to handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get webhook type from stripe
    event_type = event['type']

    # If there's a handler for it, will call it from the event map,
    # otherwise will call the default event handler
    event_handler = event_map.get(event_type, handler.handle_event)

    response = event_handler(event)
    return response
