from django.test import TestCase
from .models import Producto

class ProductoTestCase(TestCase):
    def setUp(self):
        Producto.objects.create(nombre="Producto 1", precio=10.00, stock=100)

    def test_producto_creado(self):
        producto = Producto.objects.get(nombre="Producto 1")
        self.assertEqual(producto.precio, 10.00)