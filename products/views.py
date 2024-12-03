from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
# from django.views.generic import ListView
from .models import Product, Category

# class ProductListView(ListView):
#     """A view to display paginated products."""
#     model = Product # get objects from the Product model
#     template_name = 'products/products.html'  # which html to use
#     context_object_name = 'products'  # Access the products in the template
#     paginate_by = 6  # number of products per page
#     ordering = ['name']  # ordering by name

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None # prevents error when loading the pages, without a query
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('all_products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) # pip is or and i before contains make it case insensitive
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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

