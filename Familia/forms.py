from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User


class FormTios(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    proveniente=forms.CharField(max_length=10)
    edad=forms.IntegerField()
    nacimiento=forms.DateField()

class FormHermanos(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    nacimiento=forms.DateField()

class FormPrimos(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    nacimiento=forms.DateField()

class FormViven(forms.Form):
    ciudad=forms.CharField(max_length=50)
    estado=forms.CharField(max_length=50)

class FormTrabajan(forms.Form):
    profesion=forms.CharField(max_length=50)
    titulo=forms.CharField(max_length=30)
    mail=forms.EmailField()
    activo=forms.BooleanField()

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()
 
    class Meta:
        model = User
        fields = ['username','email']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Modificar Mail')
    first_name = forms.CharField(label='Modificar Nombre')
    last_name = forms.CharField(label='Modificar Apellido')
 
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Sube tu Avatar")
