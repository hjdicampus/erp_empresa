from django.db import models

class RegistroPublico(models.Model):
    nombre_completo = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50, unique=True)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=128)

    def __str__(self):
        return self.usuario