from django.db import models
from products.models import Product

# Create your models here.

class DeliveryMethod(models.Model):
    name = models.CharField(max_length=20, unique = True)

    def __str__(self):
        return str(self.name)

class NewOrder(models.Model):
    mobille_number = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.DO_NOTHING,)
    note = models.TextField(null=True, blank=True)
    return_note = models.TextField(null=True, blank=True)
    cancel_note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True,)
    update_at = models.DateTimeField(null=True, blank=True,)
    total_price = models.IntegerField()

    def __str__(self):
        return str(self.id) 

class OrderDetails(models.Model):
    Initial = 'Initial'
    Assigned = 'Assigned'
    Pending = 'Pending'
    Complete = 'Complete'  
    Return = 'Return'
    STATUS = [
        (Initial, 'Initial'),
        (Assigned, 'Assigned'),
        (Pending, 'Pending'),
        (Return, 'Return'),
        (Complete, 'Complete'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default=Initial,
        
    )

    order_number = models.ForeignKey(NewOrder, on_delete=models.DO_NOTHING)
    sku = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    qty = models.IntegerField()