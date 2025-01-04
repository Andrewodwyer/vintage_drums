from django.shortcuts import render
from products.models import Product, Category


def index(request):
    """
    Renders the homepage with featured products, including categories,
    drum kits, and cymbals.

    **Context**
    - ``categories``: A queryset containing all product categories.
    - ``featured_drum_kits``: A queryset of the top 4 highest-rated
    drum kits, sorted by rating.
    - ``featured_cymbals``: A queryset of the top 4 highest-rated cymbals,
    filtered by categories
    ('hi_hats', 'ride_cymbal', 'crash_cymbal') and sorted by rating.

    **Template**
    :template: `home/index.html`
    """
    categories = Category.objects.all()

    # highest-rated drum kits (category: 'Drum Kit')
    featured_drum_kits = Product.objects.filter(
        category__friendly_name='Drum Kits'
    ).order_by('-rating')[:4]

    # highest-rated cymbals
    cymbal_categories = ['hi_hats', 'ride_cymbal', 'crash_cymbal']
    featured_cymbals = Product.objects.filter(
        category__name__in=cymbal_categories
    ).order_by('-rating')[:4]

    return render(request, 'home/index.html', {
        'categories': categories,
        'featured_drum_kits': featured_drum_kits,
        'featured_cymbals': featured_cymbals,
    })
