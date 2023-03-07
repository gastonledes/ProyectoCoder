from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre= models.CharField(max_length=40)
    camada= models.IntegerField()

class Estudiantes(models.Model):
    nombre=models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email = models.EmailField()
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechadeentrega = models.DateField()
    entregado = models.BooleanField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)


