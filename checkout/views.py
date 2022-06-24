from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
import stripe
from cart.contexts import cart_contents


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your cart is empty')
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    print(f'total: {total}')
    stripe_total = round(total * 100)
    print(f'stripe total: {stripe_total}')
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )


    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Sripe public key is missing!')
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)