from django.shortcuts import render
from .models import *
from django.http import *
from Familia.forms import *
from django.db.models.query_utils import *
from django import forms
from django.views.generic import *
from django.views.generic.detail import DetailView
from django.urls import *
from django.contrib.auth.forms import *
from django.contrib.auth import *
from django.contrib.auth.mixins import *
from django.contrib.auth.decorators import *

@login_required
def blog(request):
    return render(request, "blog/inicio.html", {"mensaje":"Hola Bienvenido al Blog Familiar"})
