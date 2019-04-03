from django import forms
from .models import Formulario
from .models import Materia
from .models import HabilidadBlanda

HABILIDADES_BLANDAS_CHOICES = ('1980', '1981', '1982')
MATERIAS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)
# Create your models here.
class FormularioModelForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ["comentario",]
        labels = ["¿?"]

class FormularioForm(forms.Form):
    comentario = forms.CharField()

class MateriaModelForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ["nombre",]
        labels = ["Materia",]

class MaterialForm(forms.Form):
    nombre = forms.ChoiceField(
        choices=MATERIAS_CHOICES,
    )

class HabilidadBlandaModelForm(forms.ModelForm):
    class Meta:
        model = HabilidadBlanda
        fields = ["nombre", "formulario"]
        labels = ["Habilidad Blanda", "Formulario"]

class HabilidadBlandaForm(forms.Form):
    nombre = forms.ChoiceField(
        choices=HABILIDADES_BLANDAS_CHOICES,
    )