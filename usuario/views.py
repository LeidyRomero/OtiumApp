import requests
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
#from .forms import registroUsuarioForm
from django.contrib.auth.decorators import login_required
from .models import Usuario

# Create your views here.
#def registro(request):
    #if request.method == 'POST':
        #form = registroUsuarioForm(request.POST)
        #if form.is_valid():
            #form.save()
            #nombres = form.cleaned_data.get('nombres')
            #apellidos = form.cleaned_data.get('apellidos')
            #email = form.cleaned_data.get('email')
            #universidad = form.cleaned_data.get('universidad')
            #fechaNacimiento = form.cleaned_data.get('fechaNacimiento')
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            #return redirect('home')
        #else:
            #print(form.errors)
    #else:
        #form = registroUsuarioForm()

    #return render(request, 'usuario.html', {'form': form})
def index(request):
    return render(request, 'base.html')