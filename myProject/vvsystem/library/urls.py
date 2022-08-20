from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suppliers/', views.suppliers, name='suppliers'),
    path('suppliers/<int:supplier_id>', views.supplier, name='supplier'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('search/', views.search, name='search'),
    path('clients/', views.clients, name='clients'),
    path('clients/<int:client_id>', views.client, name='client'),
    path('managers/', views.managers, name='managers'),
    path('managers/<int:manager_id>', views.manager, name='manager'),
    path('sales/', views.sales, name='sales'),
    path('sales/<int:sale_id>', views.sale, name='sale'),
    path('orders/', views.orders, name='orders'),
    path('orders/<int:order_id>', views.order, name='order'),
    path('accounts/', include('django.contrib.auth.urls')),
]
