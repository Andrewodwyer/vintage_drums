from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

def view_bag(request):
    """ A view that renders the bag contents page """
    allowed_categories = ['sticks', 'stand']  # Categories with relaxed quantity limits
    return render(request, 'bag/bag.html', {
        'allowed_categories': allowed_categories,
    })


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')  # URL to redirect back
    size = request.POST.get('size_option', None)  # Size for sticks if size_option is enabled
    
    # Get or initialize the shopping bag from the session
    bag = request.session.get('bag', {})

    # Check the product category
    category = product.category.name.lower()
    allowed_categories = ['sticks']

    # Only handle size for products in 'stick' category and if size_option is enabled
    if size and category == 'sticks' and product.size_option:
        if item_id in bag:
            # Check if the item is already in the bag and handle it as a dictionary
            if isinstance(bag[item_id], dict):
                if size in bag[item_id].get('items_by_size', {}):
                    bag[item_id]['items_by_size'][size] += quantity
                    messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
                else:
                    # Add the size to the existing product
                    bag[item_id]['items_by_size'][size] = quantity
                    messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
            else:
                # The item is stored as an integer, convert it to a dictionary for size
                bag[item_id] = {'items_by_size': {size: quantity}}
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            # If item is not already in the bag, add it with the specified size
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        # Handle products without size or for products in other categories
        if item_id in bag:
            if isinstance(bag[item_id], dict):
                # Handle items with size/material options, retain the dictionary structure
                if category in allowed_categories:
                    bag[item_id]['quantity'] += quantity

                else:
                    bag[item_id]['quantity'] = 1
            else:
                # Otherwise, handle items as a single quantity integer
                if category in allowed_categories:
                    bag[item_id] += quantity
                else:
                    bag[item_id] = 1
        else:
            # Initialize entry for item without size/material
            bag[item_id] = quantity
            messages.success(request, f"Added {product.name} to your bag!")

    # Save the updated bag back into the session
    request.session['bag'] = bag
    # messages.success(request, f"Added {product.name} to your bag!")

    # Redirect to the previous page or a default view
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'size_option' in request.POST:
        size = request.POST['size_option']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag."""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'size_option' in request.POST:
            size = request.POST['size_option']
        bag = request.session.get('bag', {})

        if size:
            if item_id in bag and size in bag[item_id].get('items_by_size', {}):
                del bag[item_id]['items_by_size'][size]
                if not bag[item_id]['items_by_size']:
                    bag.pop(item_id)
                messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
            else:
                messages.error(request, "Item or size not found in the bag.")
        else:
            if item_id in bag:
                bag.pop(item_id)
                messages.success(request, f'Removed {product.name} from your bag')
            else:
                messages.error(request, "Item not found in the bag.")

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
