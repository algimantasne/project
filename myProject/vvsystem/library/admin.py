from django.contrib import admin

# Register your models here.
from .models import Supplier, Product, Client, Sale, Expenses


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'supplier', 'price', 'quantity')



admin.site.register(Supplier)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client)
admin.site.register(Sale)
admin.site.register(Expenses)