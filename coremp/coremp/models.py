from django.db import models
from clientes.models import RegistroPublico

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_meses = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre_completo = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    fecha_contratacion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_completo

class Venta(models.Model):
    cliente = models.ForeignKey(RegistroPublico, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    nombre_facturacion = models.CharField(max_length=100)
    direccion_facturacion = models.TextField()
    metodo_pago = models.CharField(max_length=50)  # Ej. "Tarjeta", "Transferencia"

    def __str__(self):
        return f"Venta de {self.plan.nombre} a {self.cliente.nombre_completo}"