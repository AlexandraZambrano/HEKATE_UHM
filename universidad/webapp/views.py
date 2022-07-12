from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .forms import RegForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Create your vie here.
from webapp.forms import RegistroForm
from webapp.models import *


#def loginPage(request):
    #return render(request, './registration/login.html')

def docente(request):
    return render(request, 'docente.html')


@login_required
def estudiantes(request):
    estudiant = Estudiante.objects.all()
    return render(request, 'profesorcurso.html', {'estu': estudiant})

@login_required
def perfil(request):
    return render(request, 'perfil.html')

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
            return redirect('estudiante')

    else:
        formaEstudiantes = RegistroForm(instance=estudiante)

    return render(request, 'editar.html', {'forestudiante': formaEstudiantes})

@login_required
def eliminarEstudiante(request, id):
    estudiante = get_object_or_404(Estudiante, pk=id)
    if estudiante:
        estudiante.delete()
        return redirect('estudiante')

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