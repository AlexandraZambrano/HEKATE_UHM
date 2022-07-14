from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Create your vie here.
from webapp.forms import RegistroForm
from webapp.models import *


#def loginPage(request):
    #return render(request, './registration/login.html')
#def contraseña(request):
    #return render(request, 'contraseña.html')
#def contraseña(request):
    #if request.method == 'POST':
        #form = Contraseña(request.POST)
        #if form.is_valid():
            #username = form.cleaned_data.get('username')
            #form.save()
            #return redirect('/')
    #else:
        #form = Contraseña()
    #context = {'form': form}
    #return render(request,'contraseña.html', context)

def docente(request):
    return render(request, 'docente.html')


@login_required
def estudiantes(request):
    estudiant = Estudiante.objects.all()
    return render(request, 'profesorcurso.html', {'estu': estudiant})

@login_required
def perfil(request):
    asig = Asignatura.objects.all()
    return render(request, 'perfil.html', {'asignatura': asig})

@login_required
def estudianteNuevo(request):
    if request.method == 'POST':
        formaEstudiantes = RegistroForm(request.POST)
        if formaEstudiantes.is_valid():
            formaEstudiantes.save()
            return redirect('estudiante')

    else:
        formaEstudiantes = RegistroForm

        return render(request, 'NuevoEstudiante.html', {'forestudiante': formaEstudiantes})

@login_required
def editarEstudiante(request, id):
    estudiante = get_object_or_404(Estudiante, pk=id)
    if request.method == 'POST':
        formaEstudiantes = RegistroForm(request.POST, instance=estudiante)
        if formaEstudiantes.is_valid():
            formaEstudiantes.save()
            messages.success(request, "Modificado correctamente")
            return redirect('estudiante')

    else:
        formaEstudiantes = RegistroForm(instance=estudiante)

    return render(request, 'editar.html', {'forestudiante': formaEstudiantes})
""" 
@login_required
def eliminarEstudiante(request, id):
    estudiante = get_object_or_404(Estudiante, pk=id)
    if estudiante:
        estudiante.delete()
        return redirect('estudiante')
"""
@login_required
def eliminarEstudiante(request, id):
    estudiante = Estudiante.objects.get(pk=id)
    #estudiante = get_object_or_404(Estudiante, pk=id)
    #POST request
    if request.method == "POST":
        #Confirma eliminar
        estudiante.delete()
        messages.success(request, "Registro eliminado correctamente.")
        return redirect('estudiante')
    return render(request, "eliminarEstudiante.html", {'estudiante': estudiante})



@login_required
def salir(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('/')
    else:
        form = RegForm()
    context = {'form': form}
    return render(request,'registration/registration2.html', context)


@login_required
def busquedaEstudiante(request):

    return render(request, "profesorcurso.html")

@login_required
def buscar(request):

    if request.GET["estudiantito"]:

        # mensaje = "Estudiante Buscado: %r" %request.GET["estudiantito"]
        estudiante = request.GET["estudiantito"]
        if len(estudiante) > 20:
            mensaje = "Texto de búsqueda demasiado largo"
        else:
            estudiantes = Estudiante.objects.filter(nombre__icontains=estudiante)
            return render(request, "resultadoBusqueda.html", {"estudiantes": estudiantes, "query": estudiante})
    else:
        mensaje = "No has introducido nada."

    return HttpResponse(mensaje)
