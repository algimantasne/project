# from django.http import HttpResponse
from .models import Product, Supplier, Client, Sale, Expenses, Manager
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q



def index(request):
    # Suskaičiuokime keletą pagrindinių objektų
    num_products = Product.objects.all().count()
    num_suppliers = Supplier.objects.all().count()
    num_clients = Client.objects.count()
    num_managers = Manager.objects.count()
    num_sales = Sale.objects.count()
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


# def suppliers(request):
#
#     suppliers = Supplier.objects.all()
#     context = {
#         'suppliers': suppliers
#     }
#     print(suppliers)
#     return render(request, 'suppliers.html', context=context)
def suppliers(request):
    paginator = Paginator(Supplier.objects.all(), 10)
    page_number = request.GET.get('page')
    paged_suppliers = paginator.get_page(page_number)
    context = {
        'suppliers': paged_suppliers
    }
    return render(request, 'suppliers.html', context=context)


def supplier(request, supplier_id):
    single_supplier = get_object_or_404(Supplier, pk=supplier_id)
    return render(request, 'supplier.html', {'supplier': single_supplier})


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10
    template_name = 'product_list.html'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'


from django.db.models import Q

def search(request):

    query = request.GET.get('query')
    search_results = Product.objects.filter(Q(title__icontains=query) | Q(summary__icontains=query))
    return render(request, 'search.html', {'products': search_results, 'query': query})


def clients(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    print(clients)
    return render(request, 'clients.html', context=context)

def client(request, client_id):
    single_client = get_object_or_404(Client, pk=client_id)
    return render(request, 'client.html', {'client': single_client})