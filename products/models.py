from itertools import product
from django.contrib.auth.models import User
from django.db.models import Sum
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
    availability = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def avg_rating(self):
        try:
            ratings = Rating.objects.filter(product=self)
            n_of_ratings = Rating.objects.filter(product=self).count()
            sum_of_ratings = ratings.aggregate(Sum('rating'))['rating__sum']
            if sum_of_ratings:
                return sum_of_ratings/n_of_ratings
        except Rating.DoesNotExist:
            return None

    
    def total_ratings(self):
        try:
            ratings = Rating.objects.filter(product=self)
            return ratings.count()
        except Rating.DoesNotExist:
            return 0


    def rounded_rating(self):
        return math.floor(self.avg_rating)

    def availability_range(self):
        return range(self.availability)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name='rating')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()