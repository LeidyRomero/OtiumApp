from django import forms
from .models import Usuario

class registroUsuarioForm(forms.ModelForm):

    username = forms.CharField(label='Username',
                             widget=forms.TextInput(attrs={"placeholder": "Username"}))
    nombres = forms.CharField(label='Nombres',
                             widget=forms.TextInput(attrs={"placeholder": "Nombres"}))
    apellidos = forms.CharField(label='Apellidos',
                             widget=forms.TextInput(attrs={"placeholder": "Apellidos"}))
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={"placeholder": "ej@dominio.com"}))
    universidad = forms.CharField(label='Universidad',
                             widget=forms.TextInput(attrs={"placeholder": "Opcional"}))
    fechaNacimiento = forms.DateField(label='Fecha Nacimiento')
    contrasenia = forms.CharField(label='Constraseña',
                             widget=forms.TextInput(attrs={"placeholder": "Contraseña"}))
    formulario = forms.CharField(label = 'Formulario')

    class Meta:
        model = Usuario
        fields = [
            'username',
            'nombres',
            'apellidos',
            'email',
            'universidad',
            'fechaNacimiento',
            'formulario'
        ]
        widgets = {
            'contrasenia': forms.PasswordInput(),
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