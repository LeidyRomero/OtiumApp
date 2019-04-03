from django.db import models
from django import forms

# Create your models here.
#
class Usuario(models.Model):
    username = forms.CharField(max_length=20, required=True, help_text='Obligatorio.')
    nombres = forms.CharField(max_length=30, required=True, help_text='Obligatorio.')
    apellidos = forms.CharField(max_length=30, required=True, help_text='Obligatorio.')
    email = forms.EmailField(max_length=254, help_text='Obligatorio. Inserte una dirección de correo valida.')
    universidad = forms.CharField(max_length=40, required=False, help_text='Opcional.')
    fechaNacimiento = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"))

    def __str__(self):
        return '%s %s' % (self.value, self.unit)