from django import forms
from django.db import models
# Create your models here.
from formulario.models import Formulario


class Usuario(models.Model):
    username = models.CharField(max_length=20, primary_key = True)
    nombres = models.CharField(max_length=30, default = ' ')
    apellidos = models.CharField(max_length=30, default = ' ')
    email = models.EmailField(max_length=254, default = ' ')
    universidad = models.CharField(max_length=40, default = ' ')
    fechaNacimiento = models.DateField(null = True)
    contrasenia = models.CharField(max_length=250, default = ' ')

    def ___str___(self):
        return self.username