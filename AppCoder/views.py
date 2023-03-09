from django.shortcuts import render
from AppCoder.models import Curso, Profesor
from django.http import HttpResponse
from AppCoder.forms import *
# Create your views here.

def inicio(request):
    return render(request, 'inicio_ori.html')

#def cursos(request):
#     return render(request, 'cursos.html')

def estudiantes(request):
        return render(request, 'estudiantes.html')

def profesores(request):
    return render(request, 'profesores.html')

def entregables(request):
     return render(request, 'entregables.html')

def cursos(request):
     if request.method == 'POST':
          miFormulario = Cursoformulario(request.POST)

          print(miFormulario)
          
          if miFormulario.is_valid:
               
               informacion = miFormulario.cleaned_data
               
               curso= Curso(nombre=informacion['nombre'], camada=informacion['camada'])
               curso.save()
               
               return render(request, 'inicio_ori.html')
     else:
          miformulario = Cursoformulario()     
     return render(request,'cursos.html', {'miformulario' : miformulario})


def profesorformulario(request):
     if request.method == 'POST':
          miFormulario = Profesorformulario(request.POST)

          print(miFormulario)
          
          if miFormulario.is_valid:
               
               informacion = miFormulario.cleaned_data
               
               profesor= Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
               profesor.save()
               
               return render(request, 'inicio_ori.html')
     else:
          miformulario = Profesorformulario()     
     return render(request,'profesorformulario.html', {'miformulario' : miformulario})

def busquedaCamada(request):
     return render(request, 'cursos.html')

def buscar(request):
     if request.GET['camada']:
          camada = request.GET['camada']
          curso = Curso.objects.filter(camada__icontains=camada)
          return render(request, 'inicio_ori.html', {"curso" : curso, "camada": camada})
     else:
          respuesta = "No enviaste datos."

     #return HttpResponse(respuesta)
     return render(request, "inicio_ori.html", {'respuesta': respuesta})
