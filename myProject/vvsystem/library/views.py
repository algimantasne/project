# from django.http import HttpResponse
from .models import Product, Supplier, Client, Sale, Expenses, Manager
from django.shortcuts import render, get_object_or_404




def index(request):
    # Suskaičiuokime keletą pagrindinių objektų
    num_products = Product.objects.all().count()
    num_suppliers = Supplier.objects.all().count()
    # Kiek yra Client
    num_clients = Client.objects.count()
    # Kiek yra Manager
    num_managers = Manager.objects.count()
    # Kiek yra Sale
    num_sales = Sale.objects.count()
    # Kiek yra Sale
    num_expenses = Expenses.objects.count()

    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'num_products': num_products,
        'num_suppliers': num_suppliers,
        'num_clients': num_clients,
        'num_managers': num_managers,
        'num_sales': num_sales,
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

def supplier(request, supplier_id):
    single_supplier = get_object_or_404(Supplier, pk=supplier_id)
    return render(request, 'supplier.html', {'supplier': single_supplier})


