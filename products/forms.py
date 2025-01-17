from django import forms
from .models import Product, Category, DrumKitDetail
from .widgets import CustomClearableFileInput


# Form to handle drum kit details
class DrumKitDetailForm(forms.ModelForm):
    class Meta:
        model = DrumKitDetail
        fields = [
            'bass_drum_size', 'snare_drum_size', 'rack_tom_1_size',
            'rack_tom_2_size', 'rack_tom_3_size', 'floor_tom_1_size',
            'floor_tom_2_size', 'colour'
        ]


# Form to handle product details
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  # Includes all fields from the Product model

    # Custom image field with specific widget for file input
    image = forms.ImageField(
        label='Image',
        required=False,  # Image is optional
        widget=CustomClearableFileInput  # handling file input
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Populate category choices from the database and format them
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
