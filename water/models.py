from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="BIOLIFE")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="5000" )
    stock = models.PositiveIntegerField(default=0, verbose_name="1000")

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=150, verbose_name="hilol market")
    phone = models.CharField(max_length=20, verbose_name="9036701550")
    address = models.TextField(verbose_name="Vatsroy")

    def __str__(self):
        return self.name

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="invoices")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="BIOLIFE")
    total_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)
