from django.urls import path
from . import views

urlpatterns = [
    path('', views.venta_list, name='venta_list'),
    path('create/', views.venta_create, name='venta_create'),
    path('edit/<int:pk>/', views.venta_edit, name='venta_edit'),
    path('delete/<int:pk>/', views.venta_delete, name='venta_delete'),
]
