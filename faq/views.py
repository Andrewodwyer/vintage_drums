from django.shortcuts import render
from .models import FAQ

def faq_list(request):
    """
    Displays a list of frequently asked questions.

    **Context**
    - ``faqs``: A queryset of all FAQs, ordered by descending order.

    **Template**
    :template: `faq/faq_list.html`
    """
    faqs = FAQ.objects.all().order_by('-created_at')
    return render(request, 'faq/faq_list.html', {'faqs': faqs})

def privacy_policy(request):
    """
    Renders the privacy policy page.
    """
    return render(request, 'faq/privacy_policy.html')

