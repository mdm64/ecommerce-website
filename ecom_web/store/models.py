from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True)
    image = models.ImageField(default=None, upload_to='profile_pics')

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)

class OrderItem1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # orderditems = models.ForeignKey(OrderItem1, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length= 200, null=True)
    city = models.CharField(max_length=100, null = True)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
