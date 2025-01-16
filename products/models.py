from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.humanize.templatetags.humanize import intcomma


# only there audio files can be used
def validate_audio_file(file):
    valid_extensions = ['.mp3', '.wav', '.ogg']
    if not any(file.name.endswith(ext) for ext in valid_extensions):
        raise ValidationError(
            'Unsupported file extension. Allowed types: .mp3, .wav, .ogg'
        )


class Category(models.Model):
    """
    Represents a product category.

    Attributes:
        name (str): The name of the category.
        friendly_name (str): An optional friendly name for the category.
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Represents a product in the store.
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="products"
    )
    sku = models.CharField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(
        upload_to="products/", blank=True, default="default.jpg")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    link_to_official_page = models.URLField(
        max_length=1024, blank=True, null=True)
    sound_recording = models.FileField(
        upload_to="sound_clips/",
        blank=True, null=True,
        validators=[validate_audio_file]
    )
    add_custom_initial = models.CharField(
        max_length=4, blank=True, default="")
    updated_on = models.DateTimeField(auto_now=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    size_option = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name

    def formatted_price(self):
        """
        Returns the price with commas (e.g., '2,123.00')
        """
        return f"{intcomma(self.price)}"


class DrumKitDetail(models.Model):
    """
    Represents specific details for a drum kit product.
    """
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="drumkit_detail")
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


class Like(models.Model):
    """
    Represents a 'like' action from a user on a product.
    Attributes:
        user (User): The user who liked the product.
        product (Product): The product that was liked.
        date_created (datetime): The timestamp when the
        like was created.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="liked_products")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="likes")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")
    # User can like a product only once

    def __str__(self):
        return f"{self.user.username} likes {self.product.name}"
