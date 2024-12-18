from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import About, Review
from .forms import ReviewForm

def about(request):
    """Display the About page with reviews and handle review submission."""
    about_content = get_object_or_404(About)
    reviews = Review.objects.filter(approved=True, review=about_content).order_by('-rating')[:3]  # Fetch reviews for this About instance

    if request.method == "POST" and request.user.is_authenticated:
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.reviewer = request.user
            review.review = about_content  # Link the review to the correct About instance
            if 1 <= review.rating <= 5:  # Validate rating range
                review.save()
                messages.success(request, "Your review has been submitted and is awaiting approval.")
            else:
                messages.error(request, "Invalid rating. Please choose a value between 1 and 5.")
        else:
            messages.error(request, "There was an error submitting your review. Please try again.")
    else:
        review_form = ReviewForm()

    return render(request, 'about/about.html', {
        'about_content': about_content,
        'reviews': reviews,
        'review_form': review_form,
    })
