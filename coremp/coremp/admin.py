from django.contrib import admin
from .models import Producto, Plan, Departamento, Empleado

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'disponible')
    list_filter = ('disponible',)
    search_fields = ('nombre', 'descripcion')

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_mensual', 'duracion_meses', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'descripcion')

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'correo', 'departamento', 'activo')
    list_filter = ('departamento', 'activo')
    search_fields = ('nombre_completo', 'correo')