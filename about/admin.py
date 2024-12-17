from django.contrib import admin
from .models import About, Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_on')
    inlines = [ReviewInline]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review', 'reviewer', 'rating', 'approved', 'created_on')
    list_filter = ('approved', 'rating')
    search_fields = ('reviewer__username', 'body')

admin.site.register(About, AboutAdmin)
admin.site.register(Review, ReviewAdmin)