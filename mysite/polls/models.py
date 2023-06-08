from django.db import migrations, models
# Create your models here.

class Feedback(models.Model):
    email = models.CharField(max_length=40)
    text = models.TextField()

class Client(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    text = models.TextField()
    sneakers = models.CharField(max_length=40)