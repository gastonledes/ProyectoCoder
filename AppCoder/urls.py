from django.urls import path
from AppCoder import views

urlpatterns = [
    path('',views.inicio, name= 'Inicio'),
    path('cursos', views.cursos, name='Cursos'),
    path('estudiantes', views.estudiantes, name='Estudiantes'),
    path('profesores', views.profesores, name='Profesores'),
    path('entregables', views.entregables, name='Entregables'),
    #path('cursoformulario', views.cursoformulario, name= 'Cursoformulario'),
    path('profesorformulario', views.profesorformulario, name= 'Profesorformulario'),
   # path('busquedacamada', views.busquedaCamada, name='Busquedacamada'),
    path('buscar/', views.buscar),
]