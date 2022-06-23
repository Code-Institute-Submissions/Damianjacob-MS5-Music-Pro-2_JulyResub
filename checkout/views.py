from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your cart is empty')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ko2rfG5hamzYoDx7zv9iMAEgR8gT3xrBbthgOP6iwqtqPmsDk8E6Z1HkM2b7347IE12jbpdjbGdd6vH2wLeQvI800CvLgLyjy',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)