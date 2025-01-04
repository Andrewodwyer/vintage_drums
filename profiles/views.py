from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from products.models import Product


@login_required
def profile(request):
    """
    Display the user's profile page, including their order history,
    liked products, and the option to update profile information.

    **Context**
    - ``form``: The user profile form to update profile information.
    - ``orders``: The list of orders associated with the user profile.
    - ``on_profile_page``: A boolean indicating whether the user is
    on the profile page.
    - ``liked_products``: List of products the user has liked.

    **Template**
    :template: `profiles/profile.html`
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    # Get liked products from the Like model
    liked_products = Product.objects.filter(likes__user=request.user)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'liked_products': liked_products,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    Display the details of a specific past order.

    **Context**
    - ``order``: The order instance being displayed.
    - ``from_profile``: Boolean showing the order was accessed
    from the user's profile.

    **Template**
    :template: `checkout/checkout_success.html`
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
