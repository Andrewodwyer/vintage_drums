from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product

class ProductListView(ListView):
    """A view to display paginated products."""
    model = Product # fetch objects from the Product model
    template_name = 'products/products.html'  # which html to use
    context_object_name = 'products'  # Access the products in the template
    paginate_by = 6  # number of products per page
    ordering = ['name']  # ordering by name

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, id=product_id)
    # Use the related_name drumkit_detail to fetch drum kit details
    drum_kit_details = getattr(product, 'drumkit_detail', None)

    return render(request, 'products/product_detail.html', {
        'product': product,
        'drum_kit_details': drum_kit_details,
    })

