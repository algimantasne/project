from django.urls import path

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

]
