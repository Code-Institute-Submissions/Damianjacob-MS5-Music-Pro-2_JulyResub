import email
from django.db import models

# Create your models here.
class NewsletterEmail(models.Model):
    email = email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
        return email