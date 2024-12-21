from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import About, Review
from .forms import ReviewForm


def about_page(request):
    about = About.objects.first()  # Assuming a single "About" entry
    reviews = Review.objects.filter(approved=True, review=about)  # Correct field name here is 'review', not 'about'
    user_reviews = Review.objects.filter(reviewer=request.user) if request.user.is_authenticated else []

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.review = about  # Correct field name for the foreign key
            review.save()
            messages.success(request, "Review submitted for approval.")
            return redirect("about")
    else:
        form = ReviewForm()

    return render(request, "about/about.html", {
        "about": about,
        "reviews": reviews,
        "user_reviews": user_reviews,
        "form": form
    })


@login_required
def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk, reviewer=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated.")
            return redirect("about")
    else:
        form = ReviewForm(instance=review)

    return render(request, "about/review_form.html", {"form": form})


@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk, reviewer=request.user)
    review.delete()
    messages.success(request, "Review deleted.")
    return redirect("about")