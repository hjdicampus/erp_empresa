from django import forms
from clientes.models import RegistroPublico

class RegistroPublicoForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)  # Campo de contraseña oculto

    class Meta:
        model = RegistroPublico
        fields = ['nombre_completo', 'correo', 'telefono', 'contraseña']