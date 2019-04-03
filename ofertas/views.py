from django.shortcuts import render
from .models import Oferta
from .models import Empresa
from .models import Requerimiento

from django.http import Http404

# Create your views here.
def ofertasList(request):
	ofertas = Oferta.objects.order_by('titulo')
	context = {'ofertas': ofertas}
	return render(request, "oferta.html",context)

#def ofertaDetail(request, titulo=None, empresa=None):
	#try:
	    #oferta = Oferta.objects.get(titulo=titulo)
        #empresa = Empresa.objects.get(nombre = empresa)
        #requerimientos = Requerimiento.objects.get(oferta = titulo)
        #context = {
			#'oferta' : oferta,
			#'empresa' : empresa,
			#'requerimientos' : requerimientos
		#}
    #except MyModel.DoesNotExist:
        #raise Http404("No MyModel matches the given query.")

	#return render(request, "ofertaDetail.html", context)