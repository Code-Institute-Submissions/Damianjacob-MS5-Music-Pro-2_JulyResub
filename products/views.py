from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower


def products(request):
    """Returns the products page"""

    products = Product.objects.all()
    query = None
    category = None
    sort = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            print(f'sort: {sortkey}')
            sort = sortkey
            if sortkey == 'price_lth':
                sortkey = 'price'
                sort = 'Price - Low to High'
            if sortkey == 'price_htl':
                sortkey = '-price'
                sort = 'Price - High to Low'
            if sortkey == 'avg_customer_rating':
                sortkey = '-rating'
                sort = 'Average Customer Rating'
            products = products.order_by(sortkey)


        if 'category' in request.GET:
            products = products.filter(category__name__iexact=request.GET['category'])
            category = get_object_or_404(Category, name=request.GET['category'])


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
        'current_category': category,
        'current_sorting': sort,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """Returns the individual product details page"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)