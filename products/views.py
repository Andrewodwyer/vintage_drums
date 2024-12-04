from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None # prevents error when loading the pages, without a query
    categories = None
    sort_key = None 

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

            queries = Q(name__icontains=query) | Q(description__icontains=query) # pip is or and i before contains make it case insensitive
            products = products.filter(queries)
        
        # Sorting by price or rating
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            if sort_key in ['price', '-price', 'rating', '-rating']:
                products = products.order_by(sort_key) #Django's order_by() method


    # Pagination setup
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
        'current_sort': sort_key,
        'is_paginated': paginator.num_pages > 1,
        'page_obj': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, id=product_id)
    # Use the related_name drumkit_detail to get drum kit details
    drum_kit_details = getattr(product, 'drumkit_detail', None)

    return render(request, 'products/product_detail.html', {
        'product': product,
        'drum_kit_details': drum_kit_details,
    })

