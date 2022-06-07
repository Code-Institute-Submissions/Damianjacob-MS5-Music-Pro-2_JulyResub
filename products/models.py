from django.db import models
import math

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True, default=None)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    rating = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def rounded_rating(self):
        return math.floor(self.rating)

    def __str__(self):
        return self.name