from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Supplier, Client, Sale, Expenses, Manager


def index(request):
    # Suskaičiuokime keletą pagrindinių objektų
    num_product = Product.objects.all().count()
    num_supplier = Supplier.objects.all().count()

    # Kiek yra Client
    num_client = Client.objects.count()

    # Kiek yra Manager
    num_manager = Manager.objects.count()

    # Kiek yra Sale
    num_sale = Sale.objects.count()

    # Kiek yra Sale
    num_expenses = Expenses.objects.count()

    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'num_product': num_product,
        'num_supplier': num_supplier,
        'num_client': num_client,
        'num_manager': num_manager,
        'num_sale': num_sale,
        'num_expenses': num_expenses,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)