from django import forms
from .models import Review, About


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body', 'rating')
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'step': 1}),
            'body': forms.Textarea(attrs={'rows': 4}),
        }


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'content']
