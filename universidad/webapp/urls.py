from django.contrib import admin
from django.urls import path

from webapp.views import *



urlpatterns = [

    path('', estudiantes, name="estudiante"),
    path('registration/', register, name="nuevoUsuario"),
    path('docente/', docente, name="docente"),
    path('perfil/', perfil, name="perfil"),
    path('NuevoEstudiante/', estudianteNuevo, name="nuevoEstudiante"),
    path('editar/<int:id>', editarEstudiante),
    path('eliminarEstudiante/<int:id>', eliminarEstudiante, name='eliminarEstudiante'),
    path('busquedaEstudiante/', busquedaEstudiante, name='busquedaEstudiante'),
    path('buscar/', buscar, name='buscar'),
    path('salir/', salir, name='saliendo'),
    #path('contraseña/', contraseña, name='contraseña'),

]
