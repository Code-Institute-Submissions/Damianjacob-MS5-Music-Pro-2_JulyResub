from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from musicpro.settings import EMAIL_HOST_USER
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from django.template.exceptions import TemplateDoesNotExist
import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send confirmation email to the user"""
        email_host_address = EMAIL_HOST_USER
        cust_email = order.email
        print(f'cust_email: {cust_email}')
        try:
            subject = render_to_string(
                'confirmation_emails/confirmation_email_subject.txt',
                {'order': order})
        except TemplateDoesNotExist as e:
            print(f'there has been an error: {e}')
            print(f'Error message: {e.message}')
        except Exception as e:
            print(f'there has been an error: {e}')
            print(f'Error type: {type(e)}')
            print(f'Error message: {e.message}')
        else:
            print(f'No errors have occurred. subject: {subject}')

        try:
            body = render_to_string(
                'confirmation_emails/confirmation_email_body.txt',
                {'order': order})
        except Exception as e:
            print(f'There has been an error: {e}')
            print(f'Error type: {type(e)}')
            print(f'Error message: {e.message}')
        else:
            print(f'No error has occurred. body: {body}')

        try:
            send_mail(
                subject,
                body,
                email_host_address,
                [cust_email]
            )
        except Exception as e:
            print(f'There has been an error: {e}')
            print(f'Error type: {type(e)}')
            print(f'Error message: {e.message}')
        else:
            print('mail sent successfully')

    def handle_event(self, event):
        """
        Handle generic Stripe webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle Stripe payment_intent.succeeded webhook event
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details.address[field] = None

        # Update profile info if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1=shipping_details.address.line1
                profile.default_street_address2=shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid
                )

                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS:\
                        Order is already in database',
                status=200
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS\
                Created order in webhook'
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle Stripe payment_intent.payment_failed webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
