from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, 'inicio_ori.html')

def cursos(request):
     return render(request, 'cursos.html')

def estudiantes(request):
        return render(request, 'estudiantes.html')

def profesores(request):
    return render(request, 'profesores.html')

def entregables(request):
     return render(request, 'entregables.html')