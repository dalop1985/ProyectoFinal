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

# Create your views here.

@login_required
def Inicio(request):
    avatar = Avatar.objects.filter(user=request.user)
    if len(avatar) != 0:
        imagen=avatar[0].imagen.url
    else:
        imagen="/media/images/Default.jpg"
    return render(request, "Familia/inicio.html", {"imagen":imagen})

@login_required
def Familia_tios(request):
    if request.method=="POST":
        form=FormTios(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombret=info["nombre"]
            apellidot=info["apellido"]
            provenientet=info["proveniente"]
            edadt=info["edad"]
            nacimientot=info["nacimiento"]

            tiost=Tios(nombre=nombret,apellido=apellidot,proveniente=provenientet,edad=edadt,nacimiento=nacimientot)
            tiost.save()
            return render(request, 'Familia/inicio.html')
    else:
        form=FormTios()

    return render(request, 'Familia/Familia_tios.html', {"form":form})

@login_required
def Familia_hermanos(request):
    if request.method=="POST":
        form=FormHermanos(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombreh=info["nombre"]
            apellidoh=info["apellido"]
            edadh=info["edad"]
            nacimientoh=info["nacimiento"]

            hermanosh=Hermanos(nombre=nombreh,apellido=apellidoh,edad=edadh,nacimiento=nacimientoh)
            hermanosh.save()
            return render(request, 'Familia/inicio.html', {"mensaje": "Registro Creado Correctamente!!!"})
    else:
        form=FormHermanos()

    return render(request, 'Familia/Familia_hermanos.html', {"form":form})

@login_required
def Familia_primos(request):
    if request.method=="POST":
        form=FormPrimos(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombrep=info["nombre"]
            apellidop=info["apellido"]
            edadp=info["edad"]
            nacimientop=info["nacimiento"]

            primosp=Hermanos(nombre=nombrep,apellido=apellidop,edad=edadp,nacimiento=nacimientop)
            primosp.save()
            return render(request, 'Familia/inicio.html', {"mensaje": "Registro Creado Correctamente!!!"})
    else:
        form=FormHermanos()

    return render(request, 'Familia/Familia_primos.html', {"form":form})

@login_required
def Familia_lugar(request):
    if request.method=="POST":
        form=FormViven(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            ciudadv=info["ciudad"]
            estadov=info["estado"]
            
            lugarv=Viven(ciudad=ciudadv,estado=estadov)
            lugarv.save()
            return render(request, 'Familia/inicio.html', {"mensaje": "Registro Creado Correctamente!!!"})
    else:
        form=FormViven()

    return render(request, 'Familia/Familia_lugar.html', {"form":form})

@login_required
def Familia_trabajan(request):
    if request.method=="POST":
        form=FormTrabajan(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            profesiont=info["profesion"]
            titulot=info["titulo"]
            mailt=info["mail"]
            activot=info["activo"]
            
            trabajant=Trabajo(profesion=profesiont,titulo=titulot,mail=mailt,activo=activot)
            trabajant.save()
            return render(request, 'Familia/inicio.html', {"mensaje": "Registro Creado Correctamente!!!"})
    else:
        form=FormTrabajan()

    return render(request, 'Familia/Familia_trabajan.html', {"form":form})

#Terminan las páginas para agregar

#Inician las páginas de búsquedas
@login_required
def BFamilia_tios(request):
    return render(request, 'Familia/BFamilia_tios.html')

@login_required
def BFamilia_hermanos(request):
    return render(request, 'Familia/BFamilia_hermanos.html')

@login_required
def BFamilia_primos(request):
    return render(request, 'Familia/BFamilia_primos.html')

@login_required
def BFamilia_lugar(request):
    return render(request, 'Familia/BFamilia_lugar.html')

@login_required
def BFamilia_trabajan(request):
    return render(request, 'Familia/BFamilia_trabajan.html')

#Termina el segmento de las páginas de búsquedas

#Inicia el segmento de las páginas con resultados de las búsquedas
@login_required
def Btios(request):
    if "nombre" in request.GET:
        nombre=request.GET["nombre"]
        nombres=Tios.objects.filter(nombre=nombre)
        return render(request,"Familia/RBFamilia_tios.html",{"nombre":nombres})
    else:
        return render(request,"Familia/BFamilia_tios", {"mensaje":"Favor de Ingresar un Nombre Correcto!"})

@login_required
def Bhermanos(request):
    if "nombre" in request.GET:
        nombre=request.GET["nombre"]
        nombres=Hermanos.objects.filter(nombre=nombre)
        return render(request,"Familia/RBFamilia_hermanos.html",{"nombre":nombres})
    else:
        return render(request,"Familia/BFamilia_hermanos", {"mensaje":"Favor de Ingresar un Nombre Correcto!"})

@login_required
def Bprimos(request):
    if "nombre" in request.GET:
        nombre=request.GET["nombre"]
        nombres=Primos.objects.filter(nombre=nombre)
        return render(request,"Familia/RBFamilia_primos.html",{"nombre":nombres})
    else:
        return render(request,"Familia/BFamilia_primos", {"mensaje":"Favor de Ingresar un Nombre Correcto!"})

@login_required
def Blugar(request):
    if "nombre" in request.GET:
        nombre=request.GET["nombre"]
        nombres=Viven.objects.filter(ciudad=nombre)
        return render(request,"Familia/RBFamilia_lugar.html",{"nombre":nombres})
    else:
        return render(request,"Familia/BFamilia_lugar", {"mensaje":"Favor de Ingresar un Nombre Correcto!"})

@login_required
def Btrabajan(request):
    if "nombre" in request.GET:
        nombre=request.GET["nombre"]
        nombres=Trabajo.objects.filter(profesion=nombre)
        return render(request,"Familia/RBFamilia_trabajan.html",{"nombre":nombres})
    else:
        return render(request,"Familia/BFamilia_trabajan", {"mensaje":"Favor de Ingresar un Nombre Correcto!"})
#Termina el segmento de las páginas con resultados de las páginas

#Inicio del CRUD
@login_required
def leerTios(request):
    tios=Tios.objects.all()
    print(tios)
    return render (request, "Familia/leerTios.html", {"Tios":tios})

@login_required
def eliminarTios(request, id):
    tios=Tios.objects.get(id=id)
    tios.delete()
    tios=Tios.objects.all()
    return render(request, 'Familia/leerTios.html', {"mensaje":"Registro eliminado correctamente", "Tios":tios})

@login_required
def editarTios(request, id):
    tios=Tios.objects.get(id=id)
    if request.method=="POST":
        form=FormTios(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            print(info)
            info=form.cleaned_data
            tios.nombre=info["nombre"]
            tios.apellido=info["apellido"]
            tios.proveniente=info["proveniente"]
            tios.edad=info["edad"]
            tios.nacimiento=info["nacimiento"]
            tios.save()
            tios=Tios.objects.all()
            return render (request, 'Familia/leerTios.html', {"Tios":tios, "mensaje": "Edición Completada..."})
    else:
        Form=FormTios(initial={"nombre":tios.nombre,"apellido":tios.apellido,"proveniente":tios.proveniente,"edad":tios.edad,"nacimiento":tios.nacimiento})
    return render(request, "Familia/editarTios.html", {"form":Form, "Tios":tios})

#Final del CRUD

#CRUD con Clases para Hermanos
class HermanosLista(LoginRequiredMixin, ListView):
    model = Hermanos
    template_name='Familia/leerHermanos.html'

class HermanosCrear(LoginRequiredMixin, CreateView):
    model = Hermanos
    success_url = reverse_lazy('HermanosLista')
    fields = ['nombre','apellido','edad','nacimiento']

class HermanosEditar(LoginRequiredMixin, UpdateView):
    model = Hermanos
    success_url = reverse_lazy('HermanosLista')
    fields = ['nombre','apellido','edad','nacimiento']

class HermanosBorrar(LoginRequiredMixin, DeleteView):
    model = Hermanos
    success_url = reverse_lazy('HermanosLista')

class HermanosDetalle(LoginRequiredMixin, DetailView):
    model = Hermanos
    template_name='Familia/Hermanos_detail.html'
#Fin CRUD Hermanos

#CRUD con Clases para Tios
class TiosLista(LoginRequiredMixin, ListView):
    model = Tios
    template_name='Familia/leerTios.html'

class TiosCrear(LoginRequiredMixin, CreateView):
    model = Tios
    success_url = reverse_lazy('TiosLista')
    fields = ['nombre','apellido','proveniente','edad','nacimiento']

class TiosEditar(LoginRequiredMixin, UpdateView):
    model = Tios
    success_url = reverse_lazy('TiosLista')
    fields = ['nombre','apellido','proveniente','edad','nacimiento']

class TiosBorrar(LoginRequiredMixin, DeleteView):
    model = Tios
    success_url = reverse_lazy('TiosLista')

class TiosDetalle(LoginRequiredMixin, DetailView):
    model = Tios
    template_name='Familia/Tios_detail.html'
#Fin CRUD Tios

#CRUD con Clases para Primos
class PrimosLista(LoginRequiredMixin, ListView):
    model = Primos
    template_name='Familia/leerPrimos.html'

class PrimosCrear(LoginRequiredMixin, CreateView):
    model = Primos
    success_url = reverse_lazy('PrimosLista')
    fields = ['nombre','apellido','edad','nacimiento']

class PrimosEditar(LoginRequiredMixin, UpdateView):
    model = Primos
    success_url = reverse_lazy('PrimosLista')
    fields = ['nombre','apellido','edad','nacimiento']

class PrimosBorrar(LoginRequiredMixin, DeleteView):
    model = Primos
    success_url = reverse_lazy('PrimosLista')

class PrimosDetalle(LoginRequiredMixin, DetailView):
    model = Primos
    template_name='Familia/Primos_detail.html'
#Fin CRUD Primos

#CRUD con Clases para Viven
class LugarLista(LoginRequiredMixin, ListView):
    model = Viven
    template_name='Familia/leerLugar.html'

class LugarCrear(LoginRequiredMixin, CreateView):
    model = Viven
    success_url = reverse_lazy('LugarLista')
    fields = ['ciudad','estado']

class LugarEditar(LoginRequiredMixin, UpdateView):
    model = Viven
    success_url = reverse_lazy('LugarLista')
    fields = ['ciudad','estado']

class LugarBorrar(LoginRequiredMixin, DeleteView):
    model = Viven
    success_url = reverse_lazy('LugarLista')

class LugarDetalle(LoginRequiredMixin, DetailView):
    model = Viven
    template_name='Familia/Lugar_detail.html'
#Fin CRUD Viven

#CRUD con Clases para Viven
class TrabajoLista(LoginRequiredMixin, ListView):
    model = Trabajo
    template_name='Familia/leerTrabajo.html'

class TrabajoCrear(LoginRequiredMixin, CreateView):
    model = Trabajo
    success_url = reverse_lazy('TrabajoLista')
    fields = ['profesion','titulo','mail','activo']

class TrabajoEditar(LoginRequiredMixin, UpdateView):
    model = Trabajo
    success_url = reverse_lazy('TrabajoLista')
    fields = ['profesion','titulo','mail','activo']

class TrabajoBorrar(LoginRequiredMixin, DeleteView):
    model = Trabajo
    success_url = reverse_lazy('TrabajoLista')

class TrabajoDetalle(LoginRequiredMixin, DetailView):
    model = Trabajo
    template_name='Familia/Trabajo_detail.html'
#Fin CRUD Viven

#Administración del Login
def Admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            pasw = form.cleaned_data.get("password")
            validar = authenticate(username=user, password=pasw)
            if validar is not None:
                login(request, validar)
                return render (request, 'Familia/inicio.html', {'mensaje':f"Bienvenido {validar}"})
            else:
                return render (request, 'Familia/Admin_login.html', {'mensaje':'Usuario o Contraseña Incorrectas!, intenta de nuevo...', "form":form})
        else:
            return render (request, 'Familia/Admin_login.html', {'mensaje':'Usuario o Contraseña Incorrectas!, intenta de nuevo...', "form":form})
    else:
        form = AuthenticationForm()
    return render(request, "Familia/Admin_login.html", {"form":form})

#Registrando Usuarios
def Admin_registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            form.save()
            return render (request, 'Familia/inicio.html', {'mensaje':f"Usuario {user} creado Satisfactoriamente..."})
        else:
            return render (request, 'Familia/Admin_registro.html', {'mensaje':f"Error al momento de crear al Usuario", "form":form})
    else:
        form = RegistroUsuarioForm()
    return render (request, "Familia/Admin_registro.html", {"form":form})

#Editando al usuario
@login_required
def Admin_perfil(request):
    usuario=request.user
    if request.method == 'POST':
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info['email']
            usuario.first_name=info['first_name']
            usuario.last_name=info['last_name']
            usuario.save()
            return render(request, 'Familia/inicio.html', {"mensaje":"Perfil Modificado Correctamente!!!"})
        else:
            return render(request, 'Familia/Admin_update.html', {"form":form, "usuario":request.user, "mensaje":"Error al Modificar el Usuario!"})

    else:
        form = UserEditForm(instance=usuario)
        return render (request, 'Familia/Admin_update.html', {"form":form, "usuario":request.user})

@login_required
def AgregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatarv=Avatar.objects.filter(user=request.user)
            if len(avatarv)!=0:
                avatarv[0].delete()
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatar.save()
            return render(request, 'Familia/inicio.html', {"mensaje":"Avatar agregado Correctamente!!!"})
        else:
            return render(request, 'Familia/AgregarAvatar.html', {"form":form, "usuario":request.user, "mensaje":"Error al Agreagar el Avatar!"})
    else:
        form=AvatarForm()
        return render(request, "Familia/AgregarAvatar.html", {"form":form, "usuario":request.user})

@login_required
def blog(request):
    return render(request, "blog/inicio.html", {"mensaje":"Hola Bienvenido al Blog Familiar"})

