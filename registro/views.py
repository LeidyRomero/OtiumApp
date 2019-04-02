from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = registroForm(request.POST)
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
        form = registroForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def home(request):
    return render(request, '')