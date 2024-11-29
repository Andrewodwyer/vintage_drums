from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# only there audio files can be used
def validate_audio_file(file):
    valid_extensions = ['.mp3', '.wav', '.ogg']
    if not any(file.name.endswith(ext) for ext in valid_extensions):
        raise ValidationError('Unsupported file extension. Allowed types: .mp3, .wav, .ogg')


# Create your models here.


# Category

class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True, null=True) #optional friendly name

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

# Product

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")
    sku = models.CharField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(upload_to="products/", blank=True, default="default.jpg")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    link_to_official_page = models.URLField(max_length=1024, blank=True, null=True)
    sound_recording = models.FileField(upload_to="sound_clips/", blank=True, null=True, validators=[validate_audio_file])
    add_custom_initial = models.CharField(max_length=4, blank=True, default="")
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Drum Kit Details Model
class DrumKitDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="drumkit_detail")
    bass_drum_size = models.PositiveIntegerField(blank=True, null=True) 
    snare_drum_size = models.PositiveIntegerField(blank=True, null=True)  
    rack_tom_1_size = models.PositiveIntegerField(blank=True, null=True)  
    rack_tom_2_size = models.PositiveIntegerField(blank=True, null=True)  
    rack_tom_3_size = models.PositiveIntegerField(blank=True, null=True)
    floor_tom_1_size = models.PositiveIntegerField(blank=True, null=True)
    floor_tom_2_size = models.PositiveIntegerField(blank=True, null=True)
    colour = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return f"DrumKitDetail for {self.product.name}"



# Cymbal options
CYMBAL_TYPES = [
    ('ride', 'Ride'),
    ('crash', 'Crash'),
    ('hi-hat', 'Hi-Hat'),
    ('splash', 'Splash'),
]

# Cymbal Model

class CymbalDetail(models.Model):
    product = models.OneToOneField("Product", on_delete=models.CASCADE, related_name="cymbal_detail")
    size = models.PositiveIntegerField(blank=True, null=True)
    type = models.CharField(max_length=254, choices=CYMBAL_TYPES, blank=True)


    def __str__(self):
        return f"CymbalDetail for {self.product.name}"


# Stand Model
class StandDetail(models.Model):
    product = models.OneToOneField("Product", on_delete=models.CASCADE, related_name="stand_detail")
    size = models.PositiveIntegerField(blank=True, null=True) #optional size
    type = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return f"StandDetail for {self.product.name}"

# likes

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="likes")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")  # User can like a product only once
    
    def __str__(self):
        return f"{self.user.username} likes {self.product.name}"