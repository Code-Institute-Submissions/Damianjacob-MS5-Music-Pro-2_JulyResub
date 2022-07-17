from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from products.models import Product
from django.contrib import messages


def view_cart(request):
    """Returns the cart"""

    return render(request, 'cart.html')


def add_to_cart(request, item_id):
    """Add a quantity of the specified product to the cart"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    message = ''

    if item_id in cart.keys():
        message = ('You have updated the quantity of ' +
                   f'{product.name.title()} to {quantity}')
    else:
        message = (
            f'You have added {quantity} ' +
            f'{"items" if quantity > 1 else "item"} of \
                {product.name} to your cart')

    cart[item_id] = quantity

    request.session['cart'] = cart
    messages.info(request, message)
    return redirect(redirect_url)


def update_cart_item(request, item_id):
    """Update an item that is already in the cart"""

    new_quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    cart[item_id] = new_quantity

    request.session['cart'] = cart

    return redirect('view_cart')


def remove_cart_item(request, item_id):
    """Remove an item from the cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart')
        del cart[item_id]
        request.session['cart'] = cart

        messages.info(
            request,
            f'{product.name.title()} has been removed from your cart')

        return redirect('view_cart')

    except Exception as e:
        return HttpResponse(status=500)
