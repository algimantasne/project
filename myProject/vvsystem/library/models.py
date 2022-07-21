from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title = models.CharField('Name', max_length=200)
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True)
    summary = models.TextField('Summary', max_length=1000, help_text='Trumpas knygos aprašymas')
    price = models.CharField('Price, Eur', max_length=5, null=True)
    quantity = models.CharField('Quantity, pcs', max_length=5, null=True)


    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        """Nurodo konkretaus aprašymo galinį adresą"""
        return reverse('product-detail', args=[str(self.id)])




class Supplier(models.Model):
    name = models.CharField('Name', max_length=100)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('supplier-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.name)



class Client(models.Model):
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField('Last name', max_length=100)
    address = models.CharField('Address', max_length=100, null=True)
    phone = models.CharField('Phone', max_length=12, null=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name} {self.first_name}, {self.address}'


class Sale(models.Model):
    order_No = models.CharField('Order_No', max_length=200)

    def __str__(self):
        return str(self.order_No)

    def get_absolute_url(self):
        return reverse('sale-detail', args=[str(self.id)])


class Expenses(models.Model):
    amount = models.CharField('Amount', max_length=7)

    def __str__(self):
        return str(self.amount)

    def get_absolute_url(self):
        return reverse('expenses-detail', args=[str(self.id)])
