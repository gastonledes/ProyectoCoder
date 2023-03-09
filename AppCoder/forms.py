from django import forms

class Cursoformulario(forms.Form):
    nombre= forms.CharField()
    camada= forms.IntegerField()

class Profesorformulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)