from django.contrib import admin
from .models import Oferta
from .models import Empresa
from .models import Requerimiento
from .models import Atributo

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Oferta)
admin.site.register(Requerimiento)
admin.site.register(Atributo)