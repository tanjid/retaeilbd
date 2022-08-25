from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=20, unique = True)

class ProductBrand(models.Model):
    name = models.CharField(max_length=20, unique = True)

class Product(models.Model):
    name = models.CharField(max_length=20)
    sku = models.CharField(max_length=20, unique = True)
    category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING, null=True, blank=True)
    brand = models.ForeignKey(ProductBrand, on_delete=models.DO_NOTHING, null=True, blank=True)
    warranty = models.CharField(max_length=20)
    warranty_policy = models.TextField(null=True, blank=True)
    cost_price = models.IntegerField()
    sell_price = models.IntegerField()
    alert_qty = models.IntegerField()
    product_image = models.ImageField(null=True, blank=True, default="default.jpg")