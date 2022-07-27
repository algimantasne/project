from django.contrib import admin

# Register your models here.
from .models import Supplier, Product, Client, Sale, Expenses, Manager


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'supplier', 'price', 'quantity')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'manager')

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_products')


admin.site.register(Supplier)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Sale)
admin.site.register(Expenses)
admin.site.register(Manager)