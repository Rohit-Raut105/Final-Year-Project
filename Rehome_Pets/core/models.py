from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, verbose_name="Enter your phone number", null=False, blank=False)
    address = models.CharField(max_length=50, verbose_name="Enter your address", null=False, blank=False)
    def __str__(self):
        return f"{self.user.username}'s Profile"

class Products(models.Model):
    product_ID = models.AutoField(primary_key=True, verbose_name="Product ID")
    product_Name = models.CharField(max_length=80, verbose_name="Product Name", blank=False, null=False)
    product_Description = models.CharField(max_length=200, verbose_name="Product Description", blank=False, null=False)
    product_Category = models.CharField(max_length=100, verbose_name="Product Category", blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price", blank=False, null=False)
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Out of Stock', 'Out of Stock'),
        ('Discontinued', 'Discontinued'),
    ]
    def __str__(self):
        return self.product_ID
    

