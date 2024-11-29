from django.contrib import admin
from .models import Category, Product, DrumKitDetail, CymbalDetail, StandDetail, Like

# @admin.register() was used on each model instead of admin.site.register(Category)

# Category model

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "friendly_name")
    search_fields = ("name",)

# Product model

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "category", "price", "rating", "image", "updated_on", "brand")
    search_fields = ("name", "sku", "brand") #allow to seach for name, sku or brand
    list_filter = ("category", "brand") #filter by category or brand
    readonly_fields = ("updated_on",)

    ordering = ('sku',)

# DrumKitDetail model
@admin.register(DrumKitDetail)
class DrumKitDetailAdmin(admin.ModelAdmin):
    list_display = ("product", "bass_drum_size", "snare_drum_size", "rack_tom_1_size")
    search_fields = ("product__name",)

# CymbalDetail model
@admin.register(CymbalDetail)
class CymbalDetailAdmin(admin.ModelAdmin):
    list_display = ("product", "type", "size")
    search_fields = ("product__name", "type")
    list_filter = ("type",)

# StandDetail model
@admin.register(StandDetail)
class StandDetailAdmin(admin.ModelAdmin):
    list_display = ("product", "type", "size")
    search_fields = ("product__name", "type")

# Like model
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "date_created")
    search_fields = ("user__username", "product__name")
    list_filter = ("date_created",)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)