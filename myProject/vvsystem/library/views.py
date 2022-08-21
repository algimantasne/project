# from django.http import HttpResponse
from .models import Product, Supplier, Client, Sale, Order, Manager, NewOrder
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
    num_orders = Order.objects.count()
    num_newOrders = NewOrder.objects.count()

    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'num_products': num_products,
        'num_suppliers': num_suppliers,
        'num_clients': num_clients,
        'num_managers': num_managers,
        'num_sales': num_sales,
        'num_orders': num_orders,
        'num_newOrders': num_newOrders,
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


# from django.db.models import Q

def search(request):

    query = request.GET.get('query')
    search_results = Product.objects.filter(Q(title__icontains=query) | Q(summary__icontains=query))
    return render(request, 'search.html', {'products': search_results, 'query': query})


def clients(request):
    paginator = Paginator(Client.objects.all(), 10)
    page_number = request.GET.get('page')
    paged_clients = paginator.get_page(page_number)
    context = {
        'clients': paged_clients
    }
    return render(request, 'clients.html', context=context)

def client(request, client_id):
    single_client = get_object_or_404(Client, pk=client_id)
    return render(request, 'client.html', {'client': single_client})

def managers(request):
    managers = Manager.objects.all()
    context = {
        'managers': managers
    }
    print(managers)
    return render(request, 'managers.html', context=context)

def manager(request, manager_id):
    single_manager = get_object_or_404(Manager, pk=manager_id)
    return render(request, 'manager.html', {'manager': single_manager})

def sales(request):
    paginator = Paginator(Sale.objects.all(), 10)
    page_number = request.GET.get('page')
    paged_sales = paginator.get_page(page_number)
    context = {
        'sales': paged_sales
    }
    return render(request, 'sales.html', context=context)

def sale(request, sale_id):
    single_sale = get_object_or_404(Sale, pk=sale_id)
    return render(request, 'sale.html', {'sale': single_sale})

def orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'orders.html', context=context)

def order(request, order_id):
    single_order = get_object_or_404(Order, pk=order_id)
    return render(request, 'order.html', {'order': single_order})

def newOrders(request):
    newOrders = NewOrder.objects.all()
    context = {
        'newOrders': newOrders
    }
    return render(request, 'newOrders.html', context=context)

def newOrder(request, newOrder_id):
    single_newOrder = get_object_or_404(Order, pk=newOrder_id)
    return render(request, 'newOrder.html', {'newOrder': single_newOrder})
