from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class registroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'nombres',
            'apellidos',
            'email',
            'universidad',
            'fechaNacimiento',
            'username',
        ]
        labels = {
            'nombres' : 'Nombres',
            'apellidos' : 'Apellidos',
            'email' : 'Email',
            'universidad' : 'Universidad',
            'fechaNacimiento' : 'Fehca Nacimiento',
            'username': 'Username'
        }