import requests
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import registroUsuarioForm
from django.contrib.auth.decorators import login_required
from .models import Usuario

# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = registroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            nombres = form.cleaned_data.get('nombres')
            apellidos = form.cleaned_data.get('apellidos')
            email = form.cleaned_data.get('email')
            universidad = form.cleaned_data.get('universidad')
            fechaNacimiento = form.cleaned_data.get('fechaNacimiento')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = registroUsuarioForm()

    return render(request, 'usuario.html', {'form': form})

def getRole(request):
    user = request.user
    auth0user = user.social_auth.get(provider="auth0")
    accessToken = auth0user.extra_data['access_token']
    url = "https://isis2503-linkhl09.auth0.com/userinfo"
    headers = {'authorization': 'Bearer ' + accessToken}
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()
    role = userinfo['https://isis2503-linkhl09:auth0:com/role']
    return (role)