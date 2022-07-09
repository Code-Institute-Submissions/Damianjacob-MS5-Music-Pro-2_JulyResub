from django.shortcuts import (
    get_object_or_404,
    render,
    redirect,
    reverse
)
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, F
from .models import Product, Category
from .forms import ProductForm


def products(request):
    """Returns the products page"""

    products = Product.objects.all()
    categories = Category.objects.all()
    query = None
    category = None
    sort = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'price_lth':
                sortkey = 'price'
                sort = 'Price - Low to High'
            if sortkey == 'price_htl':
                sortkey = '-price'
                sort = 'Price - High to Low'
            if sortkey == 'avg_customer_rating':
                sort = 'Average Customer Rating'
                products = products.order_by(F('rating').desc(nulls_last=True))
            else:
                products = products.order_by(sortkey)

        if 'category' in request.GET:
            products = products.filter(
                category__name__iexact=request.GET['category'])
            category = get_object_or_404(
                Category, name=request.GET['category'])

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

    paginator = Paginator(products, 24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    second_last_page = page_obj.paginator.num_pages - 1
    context = {
        'products': products,
        'categories': categories,
        'page_obj': page_obj,
        'search_term': query,
        'current_category': category,
        'current_sorting': sort,
        'second_last_page': second_last_page
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """Returns the individual product details page"""

    product = get_object_or_404(Product, pk=product_id)
    referrer_page = ''

    # If the user was browsing, referrer_page
    # will allow them to return to the previous
    # page while keeping all query strings
    if 'HTTP_REFERER' in request.META:
        referrer = request.META['HTTP_REFERER']
        split_url = referrer.split('/')
        referrer_path = '/' + '/'.join(split_url[3:])
        if split_url[3] == 'products' and referrer_path != request.path:
            referrer_page = referrer

    cart = request.session.get('cart', {})
    is_in_cart = False
    quantity_in_cart = 0

    availability = product.availability
    availability_range = range(availability)

    for item_id, quantity in cart.items():
        if int(item_id) == product_id:
            is_in_cart = True
            quantity_in_cart = quantity

    context = {
        'product': product,
        'referrer_page': referrer_page,
        'is_in_cart': is_in_cart,
        'quantity_in_cart': quantity_in_cart,
        'availability': availability,
        'availability_range': availability_range, 
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have access')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please make sure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have access')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please re-check \
                    that the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have access')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
