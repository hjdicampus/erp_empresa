# compras/admin.py
from django.contrib import admin
from .models import Producto, Compra

admin.site.register(Producto)
admin.site.register(Compra)

# ventas/admin.py
from django.contrib import admin
from .models import Venta

admin.site.register(Venta)