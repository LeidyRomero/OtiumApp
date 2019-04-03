from django.shortcuts import render
from .forms import FormularioModelForm
from .forms import MateriaModelForm
from .forms import HabilidadBlandaModelForm

# Create your views here.
def formulario(request):
	form = FormularioModelForm(request.POST or None)
	form2 = MateriaModelForm(request.POST or None)
	form3 = HabilidadBlandaModelForm(request.POST or None)

	context = {
		"formularioForm": form,
		#"materiasForm": form2,
		#"habilidadesForm": form3,
	}
	if form.is_valid():
		instance = form.save(commit = False)
		instance2 = form2.save(commit = False)
		instance3 = form3.save(commit = False)
		instance.save()
		#instance2.save()
		#instance3.save()
		instance.comentario = form.cleaned_data.get("comentario")
		#instance2.nombre = form2.cleaned_data.get("nombre")
		#instance2.formulario = form2.cleaned_data.get("formulario")
		#instance3.nombre = form3.cleaned_data.get("nombre")
		#instance3.formulario = form2.cleaned_data.get("formulario")

		context = {
			"título" : "Registrado exitosamente"
		}
	return render(request, "formulario.html", context)