from django.contrib import admin
from .models import (Product, 
                     OrderItem, 
                     OrderItem1, 
                     ShippingAddress
                     )

admin.site.register(Product)

admin.site.register(OrderItem)
admin.site.register(OrderItem1)
admin.site.register(ShippingAddress)