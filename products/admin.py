from django.contrib import admin
from .models import Category, Product


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
        'rating'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)