from django.contrib import admin
from .models import Feedback


admin.site.register(Feedback)

"""class Volley(models.Model):
    image = models.ImageField(upload_to="images/", blank=True)
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=10)


class Basket(models.Model):
    image = models.ImageField(upload_to="images/", blank=True)
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=10)"""
