from django.urls import path
from . import views

urlpatterns = [
    path('', views.compra_list, name='compra_list'),
    path('create/', views.compra_create, name='compra_create'),
    path('edit/<int:pk>/', views.compra_edit, name='compra_edit'),
    path('delete/<int:pk>/', views.compra_delete, name='compra_delete'),
]