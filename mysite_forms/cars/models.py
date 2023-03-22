from django.db import models


# Create your models here.
class Review(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    review = models.CharField(max_length=500)
    stars = models.IntegerField()
