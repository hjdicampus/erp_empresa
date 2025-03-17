from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),         # Panel de administración
    path('compras/', include('compras.urls')),  # URLs de la app compras
    path('ventas/', include('ventas.urls')),    # URLs de la app ventas
]