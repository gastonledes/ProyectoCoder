from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio),
    path('cursos', views.cursos),
    path('estudiantes', views.estudiantes),
    path('profesores', views.profesores),
    path('entregables', views.entregables),
]