from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity')) # get the quantity from the form
    redirect_url = request.POST.get('redirect_url') #  url to redirect
    size = None

    # If there is a product size selected, assign it to size variable
    # future requirement
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # gets the current bag from the session or create a empty dictionary 
    bag = request.session.get('bag', {})

    if size:
        # if there is a size
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                # add quantity to the existing quantity
                bag[item_id]['items_by_size'][size] += quantity
            else:
                # add new item in this size
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}

    else:
        # the items that have no size
        if item_id in list(bag.keys()):
            # increase the quantity
            bag[item_id] += quantity
        else:
            # add the item if quantity doesn't exist
            bag[item_id] = quantity

    # update the session bag
    request.session['bag'] = bag

    # redirect
    return redirect(redirect_url)