from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """Returns the cart"""
    
    return render(request, 'cart.html')