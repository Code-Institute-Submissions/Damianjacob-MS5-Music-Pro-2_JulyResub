from django.shortcuts import render

def products(request):
    """Returns the products page"""

    return render(request, 'products/products.html')