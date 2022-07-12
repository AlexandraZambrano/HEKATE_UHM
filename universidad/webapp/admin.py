from django.contrib import admin

# Register your models here.
from webapp.models import *

admin.site.register(Estudiante)
admin.site.register(Profesor)
#admin.site.register(Curso)
admin.site.register(Asignatura)
admin.site.register(Calificaciones)
admin.site.register(EstudianteProfesor)
