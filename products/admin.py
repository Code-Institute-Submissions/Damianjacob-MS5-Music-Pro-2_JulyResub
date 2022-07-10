from django.contrib import admin
from .models import Category, Product, Rating


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    ordering = ('sku', )
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'availability'
    )

class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'rating',
        'user',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rating, RatingAdmin)
