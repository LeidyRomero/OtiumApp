from django import forms
from ..usuario import models

class IniciarForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = [
            'username',
        ]
        widgets = {
            'contrasenia': forms.PasswordInput(),
        }
        labels = {
            'username': 'Username',
            'contrasenia' : 'Contraseña'
        }