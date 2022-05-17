from django.shortcuts import render
from .models import Product, Category

def products(request):
    """Returns the products page"""
    all_products = Product.objects.all

    context = {
        'products': all_products
    }
    return render(request, 'products/products.html', context)