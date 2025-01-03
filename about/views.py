from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import About, Review
from .forms import ReviewForm, AboutForm


def about_page(request):
    """
    Displays the 'About' page with information about the company, user reviews, 
    and a form to submit new reviews for approval.

    **Context**
    - ``about``: The single instance of the About model, providing information about the company.
    - ``reviews``: A queryset of approved reviews for the 'About' page.
    - ``user_reviews``: A list of reviews submitted by the current user, if authenticated.
    - ``form``: A form to submit a new review.

    **Template**
    :template: `about/about.html`
    """
    about = About.objects.first()  # A single "About" entry
    reviews = Review.objects.filter(approved=True, review=about)
    user_reviews = Review.objects.filter(
        reviewer=request.user
        ) if request.user.is_authenticated else []

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
    """
    Allows users to edit their own reviews. The review is set as unapproved upon editing
    and requires admin approval.

    **Context**
    - ``form``: A form for editing an existing review.

    **Template**
    :template: `about/review_form.html`
    """
    review = get_object_or_404(Review, pk=pk, reviewer=request.user)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.approved = False  # review as unapproved edited
            review.save()
            messages.success(
                request, "Review updated and requires admin approval."
                )
            return redirect("about")
    else:
        form = ReviewForm(instance=review)

    return render(request, "about/review_form.html", {"form": form})


@login_required
def delete_review(request, pk):
    """
    Allows users to delete their own reviews from the 'About' page.

    **Context**
    - None, as this function performs a side effect (deletion) and redirects.

    **Template**
    :template: No specific template used for this action (redirects after deletion).
    """
    review = get_object_or_404(Review, pk=pk, reviewer=request.user)
    review.delete()
    messages.success(request, "Review deleted.")
    return redirect("about")


@login_required
def edit_about(request):
    """
    Allows superusers to edit the 'About' page content.

    **Context**
    - ``form``: A form to edit the 'About' page content.

    **Template**
    :template: `about/edit_about.html`
    """
    if not request.user.is_superuser:
        return redirect('about')

    about = About.objects.first()

    if request.method == "POST":
        form = AboutForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            messages.success(
                request, "About section updated successfully."
                )
            return redirect('about')
    else:
        form = AboutForm(instance=about)

    return render(
        request, "about/edit_about.html", {"form": form}
        )
