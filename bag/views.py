from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product

def view_bag(request):
    """ A view that renders the bag contents page """
    allowed_categories = ['sticks', 'stands']  # Categories with relaxed quantity limits
    return render(request, 'bag/bag.html', {
        'allowed_categories': allowed_categories,
    })


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')  # URL to redirect back
    size = request.POST.get('product_size', None)  # Size for sticks or sized items
    material = request.POST.get('product_material', None)  # Material for sticks
    
    # Get or initialize the shopping bag from the session
    bag = request.session.get('bag', {})

    # Check the product category
    category = product.category.name.lower()
    allowed_categories = ['sticks', 'stands']

    if size or material:
        # Handle products with size or material options
        if item_id in bag:
            # Check if the item with specific size and material already exists
            if size in bag[item_id].get('items_by_size', {}) and material in bag[item_id].get('items_by_material', {}):
                # Allow increasing quantity only for allowed categories
                if category in allowed_categories:
                    bag[item_id]['items_by_size'][size] += quantity
                else:
                    bag[item_id]['items_by_size'][size] = 1  # Restrict to 1
            else:
                # Add a new size and material entry
                bag[item_id].setdefault('items_by_size', {})
                bag[item_id].setdefault('items_by_material', {})
                bag[item_id]['items_by_size'][size] = quantity if category in allowed_categories else 1
                bag[item_id]['items_by_material'][material] = material
        else:
            # Initialize entry for item with size and material
            bag[item_id] = {
                'items_by_size': {size: quantity if category in allowed_categories else 1},
                'items_by_material': {material: material},
            }
    else:
        # Handle products without size or material
        if item_id in bag:
            # Restrict quantity to 1 unless in allowed categories
            if category in allowed_categories:
                bag[item_id] += quantity
            else:
                bag[item_id] = 1
        else:
            # Initialize entry for item without size or material
            bag[item_id] = quantity if category in allowed_categories else 1

    # Save the updated bag back into the session
    request.session['bag'] = bag
    messages.success(request, f"Added {product.name} to your bag!")

    # Redirect to the previous page or a default view
    return redirect(redirect_url)

def update_quantity(request, item_id):
    """Update the quantity or attributes of a specified product in the shopping bag."""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    size = request.POST.get('product_size', None)
    material = request.POST.get('product_material', None)

    # Get the shopping bag from the session
    bag = request.session.get('bag', {})

    if size or material:
        # Handle updates for items with size/material options
        if item_id in bag:
            if size in bag[item_id].get('items_by_size', {}) and material in bag[item_id].get('items_by_material', {}):
                if quantity > 0:
                    bag[item_id]['items_by_size'][size] = quantity
                else:
                    # Remove size/material entry if quantity is 0
                    del bag[item_id]['items_by_size'][size]
                    del bag[item_id]['items_by_material'][material]
                    if not bag[item_id]['items_by_size']:
                        bag.pop(item_id)  # Remove the product if no sizes remain
            else:
                messages.error(request, "Unable to update quantity: item not found.")
    else:
        # Handle updates for items without size/material options
        if item_id in bag:
            if quantity > 0:
                bag[item_id] = quantity
            else:
                bag.pop(item_id)

    # Save the updated bag back into the session
    request.session['bag'] = bag
    messages.success(request, f"Updated {product.name} in your bag.")
    return redirect('view_bag')