from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category, Like, DrumKitDetail
from bag.contexts import bag_contents  # Import the bag context
from .forms import ProductForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

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
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('all_products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
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
    # products = Product.objects.all().order_by('updated_on')
    paginator = Paginator(products, 6)  # 6 products per page
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sort': current_sorting,
        'is_paginated': paginator.num_pages > 1,
        'page_obj': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    bag = request.session.get('bag', {})  # Bag from session
    
    restricted_categories = ['sticks', 'stand']
    
    product_category = product.category.name.lower()
    product_in_bag = str(product_id) in bag  # Check if product is already in bag
    allow_quantity_input = product_category in restricted_categories  # Check if category allows quantity input

    drum_kit_details = getattr(product, 'drumkit_detail', None) 
    
    user_liked = request.user.is_authenticated and Like.objects.filter(product=product, user=request.user).exists()

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
    """Toggle like for a product via AJAX."""
    product = get_object_or_404(Product, id=product_id)

    # Toggle the like status
    like, created = Like.objects.get_or_create(user=request.user, product=product)
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

def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)