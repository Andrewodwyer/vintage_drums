from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.functions import Lower
from .models import Product, Category, Like, DrumKitDetail
from bag.contexts import bag_contents
from .forms import ProductForm


def all_products(request):
    """
    A view to show all products with filtering, sorting,
    and search functionalities.

    **Context**
    - ``products``: A list of products filtered by the user's
    selection (category, brand, search query).
    - ``search_term``: The user's search term if any.
    - ``current_categories``: Categories the user has filtered by.
    - ``current_sort``: Current sorting method.
    - ``is_paginated``: Boolean indicating if pagination is applied.
    - ``page_obj``: The paginated list of products.
    - ``prev_url``: URL for the previous page in pagination (if exists).
    - ``next_url``: URL for the next page in pagination (if exists).

    **Template**
    :template: `products/products.html`
    """

    products = Product.objects.all()
    query = None  # prevents error when loading the pages, without a query
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'brand' in request.GET:
            brand = request.GET['brand']
            products = products.filter(brand__iexact=brand)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse('all_products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
                )
            products = products.filter(queries)

        # Sorting by price or rating
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    # Pagination setup
    paginator = Paginator(products, 6)  # 6 products per page
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    # Prepare pagination URLs for previous and next
    base_url = request.path  # current path
    current_params = request.GET.copy()
    # Get existing query parameters from the request

    prev_url = None
    next_url = None

    # If there's a previous page, generate the previous page URL
    if products.has_previous():
        current_params['page'] = products.previous_page_number()
        prev_url = f"{base_url}?{current_params.urlencode()}"

    # If there's a next page, generate the next page URL
    if products.has_next():
        current_params['page'] = products.next_page_number()
        next_url = f"{base_url}?{current_params.urlencode()}"

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sort': current_sorting,
        'is_paginated': paginator.num_pages > 1,
        'page_obj': products,
        'prev_url': prev_url,
        'next_url': next_url,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    Displays the detailed view of a specific product.

    **Context**
    - ``product``: The product instance.
    - ``product_in_bag``: Boolean indicating whether the product is
    in the user's shopping bag.
    - ``drum_kit_details``: Drum kit details if the product is a drum kit.
    - ``allow_quantity_input``: Boolean indicating whether the user can
    input quantity for the product.
    - ``user_liked``: Boolean indicating whether the user has liked the
    product.

    **Template**
    :template: `products/product_detail.html`
    """

    product = get_object_or_404(Product, id=product_id)
    bag = request.session.get('bag', {})  # Bag from session

    restricted_categories = ['sticks', 'stand']

    product_category = product.category.name.lower()
    product_in_bag = str(product_id) in bag
    # Check if product is already in bag
    allow_quantity_input = product_category in restricted_categories
    # Check if category allows quantity input

    drum_kit_details = getattr(product, 'drumkit_detail', None)

    user_liked = request.user.is_authenticated and Like.objects.filter(
        product=product, user=request.user).exists()

    context = {
        'product': product,
        'product_in_bag': product_in_bag,
        'drum_kit_details': drum_kit_details,
        'allow_quantity_input': allow_quantity_input,
        'user_liked': user_liked,
        'restricted_categories': restricted_categories,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def toggle_like(request, product_id):
    """
    Toggle like status for a product using AJAX.

    **Returns**
    - ``user_liked``: Boolean indicating if the user has liked the product.
    - ``like_count``: The total number of likes the product has received.
    """
    product = get_object_or_404(Product, id=product_id)

    # Toggle the like status
    like, created = Like.objects.get_or_create(
        user=request.user, product=product)
    if not created:
        like.delete()  # Unlike the product
        user_liked = False
    else:
        user_liked = True

    # Get the updated like count
    like_count = product.likes.count()

    return JsonResponse({
        'user_liked': user_liked,
        'like_count': like_count,
    })


@login_required
def add_product(request):
    """
    Add a new product to the store. Superuser only.

    **Template**
    :template: `products/add_product.html`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
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
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit an existing product in the store. Superuser only.

    **Template**
    :template: `products/edit_product.html`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
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
                'Failed to update product. Please ensure the form is valid.'
            )
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
    """
    Delete a product from the store. Superuser only.

    **Redirects**
    - Redirects to the all products page after deletion.

    **Messages**
    - Success message indicating the product was deleted.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('all_products'))
