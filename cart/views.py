from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """Returns the cart"""
    
    return render(request, 'cart.html')


def add_to_cart(request, item_id):
    """Add a quantity of the specified product to the cart"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(f'cart: {request.session["cart"]}')
    return redirect(redirect_url)


def update_cart_item(request, item_id):
    """Update an item that is already in the cart"""

    new_quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    cart[item_id] = new_quantity

    request.session['cart'] = cart

    return redirect('view_cart')