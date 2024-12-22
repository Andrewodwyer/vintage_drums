from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    profile_image = models.ImageField(upload_to="about/", blank=True, default="default.jpg")
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField()

    def __str__(self):
        return self.title


class Review(models.Model):
    review = models.ForeignKey(About, on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    body = RichTextField()
    rating = models.PositiveSmallIntegerField(default=5) 
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review by {self.reviewer} - {self.rating} Stars"
