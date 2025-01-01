from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=2)
    stock = models.IntegerField()
    available = models.BooleanField()
    product_id = models.IntegerField()
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

