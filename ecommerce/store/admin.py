from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)