from django import forms
from django.db import models
# Create your models here.
from formulario.models import Formulario


class Usuario(models.Model):
    username = models.CharField(max_length=20, primary_key = True, help_text='Obligatorio.')
    nombres = models.CharField(max_length=30, help_text='Obligatorio.')
    apellidos = models.CharField(max_length=30, help_text='Obligatorio.')
    email = models.EmailField(max_length=254, help_text='Obligatorio. Inserte una dirección de correo valida.')
    universidad = models.CharField(max_length=40, help_text='Opcional.')
    fechaNacimiento = models.DateField()
    contrasenia = models.CharField(max_length=250)
    formulario = models.OneToOneField(
        Formulario ,
        on_delete = models.CASCADE
    )

    def ___str___(self):
        return self.username