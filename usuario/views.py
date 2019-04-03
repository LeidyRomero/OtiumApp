import requests
from django.shortcuts import render, redirect
from .forms import registroUsuarioForm
from .models import Usuario

#Create your views here.
def registro(request):
    if request.method == 'POST':
        form = registroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            form = registroUsuarioForm()
            return redirect(requests, 'formulario.html')
        else:
            print(form.errors)
    else:
        form = registroUsuarioForm()

    return render(request, 'registro.html', {'form': form})

def index(request):
    return render(request, 'base.html')