from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import About, Review
from .forms import ReviewForm

@login_required
def about(request):
    """Display the About page with reviews."""
    about_content = get_object_or_404(About)
    reviews = about_content.reviews.filter(approved=True).order_by('-created_on')

    # Review Form Submission
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.reviewer = request.user
            review.review = about_content
            review.save()
            messages.success(request, "Your review has been submitted and is awaiting approval.")
        else:
            messages.error(request, "There was an error submitting your review. Please try again.")
    else:
        review_form = ReviewForm()

    return render(request, 'about/about.html', {
        'about_content': about_content,
        'reviews': reviews,
        'review_form': review_form,
    })
