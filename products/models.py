from django.db import models
from django.forms import DecimalField, IntegerField

# Create your models here.
class Products(models.Model)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = DecimalField(max_digits=4, decimal_places=2)
    inventory_quantity = IntegerField()
    