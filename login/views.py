from django.shortcuts import render
#from .forms import IniciarForm
#from usuario.models import Usuario


# Create your views here.
def login(request):
    form = IniciarForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        contrasenia = form.cleaned_data.get("contrasenia")

        usuario = Usuario.objects.get(username = username, contrasenia = contrasenia)
        form = IniciarForm()
    else:
        print(form.errors)

    return render(request, 'login.html', {'form': form})