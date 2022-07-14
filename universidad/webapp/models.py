from django.contrib.auth.models import User
from django.db import models

# Create your models here.
"""class Curso(models.Model):
    nivel= [
        ('1'),
        ('3')
    ]
    nivel = models.IntegerField(null=True, choices=nivel)

    def __str__(self):
        return f'Curso {self.nivel}'"""
"""
class Profesor(models.Model):
    apellido_1 = models.CharField(max_length=100, null=False)
    apellido_2 = models.CharField(max_length=100, null=True)
    nombre = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=True)
    def __str__(self):
        return f'Profesor {self.id}: {self.nombre} {self.apellido_1}'
"""

class Asignatura(models.Model):
    # CONECTAR CON foreignKey --> profesor
    nombre_asignatura = models.CharField(max_length=100, null=False)
    # Profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'Asignatura {self.id}: {self.nombre_asignatura} {self.user}'

class Estudiante(models.Model):
    apellido_1 = models.CharField(max_length=100, null=False)
    apellido_2 = models.CharField(max_length=100, null=True)
    nombre = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    curso = models.IntegerField(null=True)
    nota = models.FloatField(default=0)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'Estudiante {self.id}: {self.nombre} {self.apellido_1} {self.curso} {self.apellido_2} {self.email} {self.nota}'

    # REVISAR lo de la primaryKey  *otras propiedades*
     #category = models.ForeignKey(Curso, related_name="Estudiante", blank=True, null=True,

class Calificaciones(models.Model):
    estudiante = models.ManyToManyField(Estudiante)
    asignatura = models.ManyToManyField(Asignatura)
    puntuacion = models.FloatField(max_length=100, null=False)
    def __str__(self):
        return f'Calificaciones {self.id}: {self.estudiante} {self.asignatura}'
""" 
class EstudianteProfesor(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)
    estudiante = models.ManyToManyField(Estudiante)
    # curso = models.CharField(max_length=10, null=False, default='Palomitas')

    def __str__(self):
        return f'EstudianteProfesor {self.id}: {self.profesor} {self.estudiante} {self.curso}'
"""







