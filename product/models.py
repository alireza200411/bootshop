from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify


class Product(models.Model):
    brand = models.CharField(max_length=60)
    model = models.CharField(max_length=70)
    date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=12, decimal_places=3, validators=[MinValueValidator(0)])
    slug = models.SlugField()
    stock = models.IntegerField()
    view = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.model)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/product')

    def __str__(self):
        return self.product.model
