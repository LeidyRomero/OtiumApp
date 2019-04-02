from django.db import models
import formulario

# Create your models here.
class Formulario(models.Model):
    class Meta:
        comentario = models.TextField(blank = True)
        #materias = ArrayField(models.ForeignKey(Materia, on_delete = models.CASCADE, related_name = 'nombre_materia'))
        #habilidadesBlandas = ArrayField(models.ForeignKey(HabilidadBlanda, on_delete=models.CASCADE, related_name='nombre_habilidad'))

class Materia(models.Model):
    class Meta:
        nombre = models.charField(max_length = 64)




class HabilidadBlanda(models.Model):
    class Meta:
        nombre = models.charField(max_length = 64)

