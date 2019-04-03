from django import forms
from .models import Usuario

class registroUsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = [
            'username',
            'nombres',
            'apellidos',
            'email',
            'universidad',
            'fechaNacimiento'
        ]
        widgets = {
            'contraseña': forms.PasswordInput(),
        }
        labels = {
            'username': 'Username',
            'nombres' : 'Nombres',
            'apellidos' : 'Apellidos',
            'email' : 'Email',
            'universidad' : 'Universidad',
            'fechaNacimiento' : 'Fecha Nacimiento',
            'contraseña' : 'contraseña'
        }