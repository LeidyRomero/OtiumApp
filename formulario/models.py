from django.db import models

# Create your models here.

class Formulario(models.Model):
    comentario = models.TextField(blank=True)
    materias = models.TextField["Algorítmica y Programación I", "Algorítmica y Programación II," \
                                "Matemática Estructural","Fundamentos de Infraestructura Tecnológica"
                                "Lenguajes y Máquinas", "Estructura de Datos",
                                "Sistemas Transaccionales", "Desarrollo de SW en Equipo"
                                "Diseño y Análilsis de Algoritmos", "TI en las Organizaciones",
                                "Cálculos","Arquitectura Empresarial", "Físicas",
                                "Infraestructura Computacional", "Arquitectura y Diseño de SW",
                                "Diseño de Productos e Innovación en TI","Modelado, Simulación y Optimización",
                                "Sistemas Empresariales","Programación con Tecnologías Web",
                                "Infraestructura de Comunicaciones", "Inteligencia de Negocios",
                                "Construcción de Aplicaciones Móviles"]
    habilidadesBlandas = models.TextField["Adaptabilidad", "Comunicación", "Resolver problemas"
                                          "Creatividad", "Relaciones interpersonales", "Trabajo en equipo"
                                          "Paciencia", "Escritura"]



class Materia(models.Model):
    nombre = models.charField(max_length=64)


class HabilidadBlanda(models.Model):
    nombre = models.charField(max_length=64)