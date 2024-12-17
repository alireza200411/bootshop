from django.db import models


class Product(models.Model):
    brand = models.CharField(max_length=60)
    model = models.CharField(max_length=70)

