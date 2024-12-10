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

    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        category = product.category.name

        if isinstance(item_data, int):
            # Item without size or material
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            # Item with size and/or material
            if 'items_by_size' in item_data:
                for size, quantity in item_data['items_by_size'].items():
                    total += quantity * product.price
                    product_count += quantity
                    bag_items.append({
                        'item_id': f"{item_id}-{size}",
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                        'total_price': quantity * product.price,
                    })

        # Determine delivery rates
        category_delivery_rate = settings.DELIVERY_RATES.get(category, 0)
        highest_delivery_rate = max(highest_delivery_rate, category_delivery_rate)

        if category == settings.DELIVERY_AND_INSTALLATION:
            drum_kit_in_bag = True

    # Delivery cost calculation
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
