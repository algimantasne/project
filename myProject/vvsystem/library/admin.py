from django.contrib import admin

# Register your models here.
from .models import Supplier, Product, Client, Sale, Order, Manager, ProductInstance

class ProductInstanceInline(admin.TabularInline):
    model = ProductInstance
    extra = 0 # išjungia placeholder'ius
    # can_delete = False   ## padaro, kad knygų modelyje nebutu galima istrinti

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ProductInstanceInline]

class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'manager')

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductInstanceAdmin(admin.ModelAdmin):
    list_display = ('product', 'status')
    list_filter = ['status']
    search_fields = ['product__title']
    # list_editable = ['status']   ### egzempliorių sąraše galima būtų redaguot

    fieldsets = (
        ('General', {'fields': ['product']}),
        ('Availability', {'fields': ['status']}),
    )
#
# class SaleAdmin(admin.ModelAdmin):
#     list_display = ['order_No', 'date', 'product', 'quantity']

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Sale)
# admin.site.register(Sale, SaleAdmin)
admin.site.register(Order)
admin.site.register(Manager)
admin.site.register(ProductInstance, ProductInstanceAdmin)