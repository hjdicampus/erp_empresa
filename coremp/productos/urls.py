from django.urls import path
from .views import producto_list

urlpatterns = [
    path('', producto_list, name='producto_list'),
]