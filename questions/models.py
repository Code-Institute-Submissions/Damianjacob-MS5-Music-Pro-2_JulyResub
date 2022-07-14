from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class UserQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name='questions')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
        related_name='questions')
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    has_answer = models.BooleanField(default=False)

    def __str__(self):
        return f'Question by {self.user}'


class OwnerAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name='answers')
    question = models.ForeignKey(UserQuestion, on_delete=models.CASCADE,
        related_name='answers')
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f'Answer by {self.user}'