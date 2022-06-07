from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def products(request):
    """Returns the products page"""

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search keyword!")
                return redirect(reverse('products'))
            
            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )
            products = products.filter(queries)

    paginator = Paginator(products, 36)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'search_term': query,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """Returns the individual product details page"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)