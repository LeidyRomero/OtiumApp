from django.db import models

# Create your models here.
class Login(models.Model):
	correo = models.CharField(max_length = 256, primary_key = True)
	contrasenia = models.CharField(max_length = 256)

def __str__(self):
	return self.correo