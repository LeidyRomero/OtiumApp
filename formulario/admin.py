from django.contrib import admin
from .models import Formulario
from .models import Materia
from .models import HabilidadBlanda
# Register your models here.
admin.site.register(Formulario)
admin.site.register(Materia)
admin.site.register(HabilidadBlanda)