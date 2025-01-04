from django.contrib import admin
from .models import Category, Product, DrumKitDetail, Like


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "friendly_name")
    search_fields = ("name",)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sku",
        "category",
        "price",
        "rating",
        "image",
        "updated_on",
        "brand"
    )
    search_fields = ("name", "sku", "brand")
    list_filter = ("category", "brand")
    readonly_fields = ("updated_on",)

    ordering = ('sku',)


# DrumKitDetail model
@admin.register(DrumKitDetail)
class DrumKitDetailAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "bass_drum_size",
        "snare_drum_size",
        "rack_tom_1_size"
    )
    search_fields = ("product__name",)


# Like model
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "date_created")
    search_fields = ("user__username", "product__name")
    list_filter = ("date_created",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
