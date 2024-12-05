from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    highest_delivery_rate = 0
    drum_kit_in_bag = False

    # Retrieve the bag from the session
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        
        if isinstance(item_data, int):
            # Single quantity
            quantity = item_data
            total += quantity * product.price
            product_count += quantity

            # Get category and determine delivery rate
            category = product.category.name
            category_delivery_rate = settings.DELIVERY_RATES.get(category, 0)
            highest_delivery_rate = max(highest_delivery_rate, category_delivery_rate)
            
            # Check for drum kits
            if category == settings.DELIVERY_AND_INSTALLATION:
                drum_kit_in_bag = True

            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
        else:
            # Items with size differentiation
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity

                # Get category and determine delivery rate
                category = product.category.name
                category_delivery_rate = settings.DELIVERY_RATES.get(category, 0)
                highest_delivery_rate = max(highest_delivery_rate, category_delivery_rate)
                
                # Check for drum kits
                if category == settings.DELIVERY_AND_INSTALLATION:
                    drum_kit_in_bag = True

                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    # Determine delivery cost
    if drum_kit_in_bag or total >= settings.FREE_DELIVERY_THRESHOLD:
        delivery = 0
        free_delivery_delta = 0
    else:
        delivery = highest_delivery_rate
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
