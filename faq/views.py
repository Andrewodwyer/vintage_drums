from django.shortcuts import render
from .models import FAQ

def faq_list(request):
    faqs = FAQ.objects.all().order_by('-created_at')
    return render(request, 'faq/faq_list.html', {'faqs': faqs})

def privacy_policy(request):
    return render(request, 'faq/privacy_policy.html')
