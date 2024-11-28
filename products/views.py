from django.shortcuts import render, get_object_or_404
from .models import Product

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
    # Check if the product is in the 'drum_kit' category
    if product.category.name == 'drum_kit' and product.drum_kit_detail:
        drum_kit_details = product.drum_kit_detail
    else:
        drum_kit_details = None

    return render(request, 'product_detail.html', {
        'product': product,
        'drum_kit_details': drum_kit_details,
    })
