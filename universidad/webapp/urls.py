from django.contrib import admin
from django.urls import path

from webapp.views import *

urlpatterns = [
    #path('', loginPage, name="loginPage"),
    #path('registration/', registration, name="registro"),

    path('', estudiantes, name="estudiante"),
    path('registration/', register, name="nuevoUsuario"),
    path('docente/', docente, name="docente"),
    path('perfil/', perfil, name="perfil"),
    path('NuevoEstudiante/', estudianteNuevo, name="nuevoEstudiante"),
    path('editar/<int:id>', editarEstudiante),
    path('eliminarestudiante/<int:id>', eliminarEstudiante),
    path('salir/', salir, name='saliendo'),
]
