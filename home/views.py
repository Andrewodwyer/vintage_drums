from django.shortcuts import render
from products.models import Product, Category

def index(request):
    # Fetch all categories to display in the categories section
    categories = Category.objects.all()

    # Get the top 4 highest-rated drum kits (category: 'Drum Kit')
    featured_drum_kits = Product.objects.filter(category__friendly_name='Drum Kit').order_by('-rating')[:4]

    # Get the top 4 highest-rated cymbals (category: 'Cymbal')
    featured_cymbals = Product.objects.filter(category__friendly_name='Cymbal').order_by('-rating')[:4]

    # Pass the categories and featured drum kits and cymbals to the template
    return render(request, 'home/index.html', {
        'categories': categories,
        'featured_drum_kits': featured_drum_kits,
        'featured_cymbals': featured_cymbals,
    })



