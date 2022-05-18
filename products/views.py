from django.shortcuts import render
from .models import Product, Category
from django.core.paginator import Paginator

def products(request):
    """Returns the products page"""
    all_products = Product.objects.all()
    paginator = Paginator(all_products, 36)

    

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'products/products.html', context)