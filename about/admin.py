from django.contrib import admin
from .models import About, Review


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_on']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['reviewer', 'rating', 'approved', 'created_on']
    list_filter = ['approved', 'rating']
    search_fields = ['reviewer__username', 'body']
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
