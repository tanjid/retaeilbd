from django.db import models
from products.models import Product
# Create your models here.

class Purchase(models.Model):
    sku = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    qty = models.IntegerField()
    note = models.TextField(null=True, blank=True)