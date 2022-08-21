from django.db import models
from django.urls import reverse
import uuid
from django.forms import ModelForm


class Product(models.Model):
    title = models.CharField('Product', max_length=200)
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, related_name='products', null=True)
    summary = models.TextField('Summary', max_length=1000, help_text='Product information')
    price = models.CharField('Price, Eur', max_length=5, null=True)
    quantity = models.CharField('Quantity, pcs', max_length=5, null=True)
    cover = models.ImageField('Cover', upload_to='covers', null=True, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Nurodo konkretaus aprašymo galinį adresą"""
        return reverse('product-detail', args=[str(self.id)])


class Supplier(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', max_length=2000, default='')
    address = models.CharField('Address', max_length=100, null=True)
    phone = models.CharField('Phone', max_length=20, null=True)
    email_address = models.CharField('Email', max_length=100, null=True)

    def get_absolute_url(self):
        return reverse('supplier-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Client(models.Model):
    client_name = models.CharField('Name', max_length=100, null=True)
    address = models.CharField('Address', max_length=100, null=True)
    phone = models.CharField('Phone', max_length=12, null=True)
    email_address = models.CharField('Email', max_length=100, null=True)
    manager = models.ForeignKey('Manager', on_delete=models.SET_NULL, related_name='clients', null=True)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self):
        return self.client_name


class Sale(models.Model):
    order_No = models.CharField('Order_No', max_length=200)
    date = models.DateTimeField('Date', null=True)
    client_name = models.ForeignKey('Client', on_delete=models.SET_NULL, related_name='sales', null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.CharField('Price, Eur/pcs', max_length=5, null=True)
    quantity = models.CharField('Quantity, pcs', max_length=5, null=True)

    def __str__(self):
        return str(self.order_No)

    def get_absolute_url(self):
        return reverse('sale-detail', args=[str(self.id)])



    def total_price(self):
        return round(float(self.quantity) * float(self.price))



class Order(models.Model):
    numb = models.CharField('Numb', max_length=20, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.CharField('Price, Eur', max_length=5, null=True)
    quantity = models.CharField('Quantity, pcs', max_length=5, null=True)
    client_name = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return str(self.numb)

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])


class NewOrder(models.Model):
    newOrder_No = models.CharField('NewOrder_No', max_length=200)
    description = models.TextField('Description', max_length=2000, default='')

    def __str__(self):
        return str(self.newOrder_No)

    def get_absolute_url(self):
        return reverse('neworder-detail', args=[str(self.id)])



class Manager(models.Model):
    manager_name = models.CharField('Manager name', max_length=100, null=True)
    address = models.CharField('Address', max_length=100, null=True)
    phone = models.CharField('Phone', max_length=12, null=True)
    email_address = models.CharField('Email', max_length=100, null=True)

    class Meta:
        ordering = ['manager_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('manager-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.manager_name}, {self.address}'



class ProductInstance(models.Model):
    """Modelis, aprašantis konkrečios Product būseną"""
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

    LOAN_STATUS = (
        ('a', 'In stock'),
        ('p', 'Reserved'),
        ('g', 'Not available for sale'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Status',
    )
    #
    # class Meta:
    #     ordering = ['due_back']

    def __str__(self):
        return f'{self.product.title}'

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('productinstance-detail', args=[str(self.id)])