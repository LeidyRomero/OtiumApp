from django import forms
from django.db import models
# Create your models here.
from formulario.models import Formulario


class Usuario(models.Model):
    username = models.CharField(max_length=20, required=True, help_text='Obligatorio.')
    nombres = models.CharField(max_length=30, required=True, help_text='Obligatorio.')
    apellidos = models.CharField(max_length=30, required=True, help_text='Obligatorio.')
    email = models.EmailField(max_length=254, help_text='Obligatorio. Inserte una dirección de correo valida.')
    universidad = models.CharField(max_length=40, required=False, help_text='Opcional.')
    fechaNacimiento = models.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"))
    contrasenia = models.CharField(widget=forms.PasswordInput()
    formulario = models.OneToOneField(
        Formulario ,
        on_delete = models.CASCADE ,
        primary_key = True ,
    )

    def ___str___(self):
        return self.username