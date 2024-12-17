from django import forms
from .models import Review


RATING_CHOICES = [
    (1, '1 Star'),
    (2, '2 Stars'),
    (3, '3 Stars'),
    (4, '4 Stars'),
    (5, '5 Stars'),
]

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=RATING_CHOICES, 
        widget=forms.RadioSelect
    )

    class Meta:
        model = Review
        fields = ['body', 'rating']  # Add 'rating' to the list of fields
