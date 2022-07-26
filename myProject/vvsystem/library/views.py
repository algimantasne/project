from django.http import HttpResponse
from .models import Product, Supplier, Client, Sale, Expenses, Manager
from django.shortcuts import render, get_object_or_404


def supplier(request, supplier_id):
    single_supplier = get_object_or_404(Supplier, pk=supplier_id)
    return render(request, 'supplier.html', {'author': single_supplier})



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


def suppliers(request):
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers
    }
    print(suppliers)
    return render(request, 'suppliers.html', context=context)


