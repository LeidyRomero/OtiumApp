from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registroForm(UserCreationForm):
    username = forms.CharField(max_length= 20, required = true, help_text='Obligatorio.')
    nombres = forms.CharField(max_length=30, required = true, help_text='Obligatorio.')
    apellidos = forms.CharField(max_length=30, required=true, help_text='Obligatorio.')
    email = forms.EmailField(max_length=254, help_text='Obligatorio. Inserte una dirección de correo valida.')
    universidad = forms.CharField(max_length=40, required=true, help_text='Opcional.', null = true)
    fechaNacimiento = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"))

    class Meta:
        model = Usuario
        #Si se putea, poner la coma al final de los fields.
        fields = ('nombres', 'apellidos', 'email', 'universidad', 'fechaNacimiento', 'username', 'password1', 'password2')