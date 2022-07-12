from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, EmailInput

from webapp.models import *


class RegistroForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
                   ]
        labels = {
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'email':'Correo',

        }

        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }