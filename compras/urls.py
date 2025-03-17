# compras/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.compra_list, name='compra_list'),
    path('create/', views.compra_create, name='compra_create'),
    path('edit/<int:pk>/', views.compra_edit, name='compra_edit'),
    path('delete/<int:pk>/', views.compra_delete, name='compra_delete'),
]

# ventas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.venta_list, name='venta_list'),
    path('create/', views.venta_create, name='venta_create'),
    path('edit/<int:pk>/', views.venta_edit, name='venta_edit'),
    path('delete/<int:pk>/', views.venta_delete, name='venta_delete'),
]