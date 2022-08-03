from django.contrib import admin

# Register your models here.

from django.contrib import admin

from inventory.models import Product, Brand

admin.site.register(Product)
admin.site.register(Brand)