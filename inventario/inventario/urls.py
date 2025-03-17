from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ventas/', include('ventas.urls')),
    path('compras/', include('compras.urls')),
    path('', lambda request: redirect('ventas/')),  # Redirige a /ventas/
]