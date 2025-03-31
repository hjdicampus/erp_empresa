from django.http import HttpResponse
from .models import Producto

def producto_list(request):
    return HttpResponse("Lista de productos")