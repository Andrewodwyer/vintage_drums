from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from django.utils.numberformat import format


def bag_contents(request):

    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    drum_kit_in_bag = False
    highest_delivery_rate = Decimal('0.00')

    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        category = product.category.name.lower()  # Ensure case-insensitivity

        if isinstance(item_data, int):
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'total_price': item_data * product.price,
            })
        elif 'items_by_size' in item_data:
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'total_price': quantity * product.price,
                })

        # Update highest delivery rate
        category_delivery_rate = Decimal(
            settings.DELIVERY_RATES.get(category, 0)
            )
        highest_delivery_rate = max(
            highest_delivery_rate, category_delivery_rate
            )

        # Check if drum kit is in the bag
        if category == settings.DELIVERY_AND_INSTALLATION:
            drum_kit_in_bag = True

    # Delivery cost calculation
    if drum_kit_in_bag or total >= settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')
    else:
        delivery = highest_delivery_rate
        free_delivery_delta = Decimal(
            settings.FREE_DELIVERY_THRESHOLD
            ) - total

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
