from django.contrib import admin
from .models import RegistroPublico

class RegistroPublicoAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'usuario', 'correo', 'telefono']
    list_filter = ['correo']

admin.site.register(RegistroPublico, RegistroPublicoAdmin)