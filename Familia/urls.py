from django.urls import path
from Familia.views import *
from django.db.models.query_utils import *
from django.contrib.auth.views import *

urlpatterns = [
    path('Familia_tios/',Familia_tios, name="Tios"),
    path('Familia_hermanos/',Familia_hermanos, name="Hermanos"),
    path('Familia_primos/',Familia_primos, name="Primos"),
    path('Familia_lugar/',Familia_lugar, name="Lugar"),
    path('Familia_trabajan/',Familia_trabajan, name="Trabajan"),
    path('BFamilia_tios/',BFamilia_tios, name="BFamilia_tios" ),
    path('Btios/',Btios, name="Btios"),
    path('BFamilia_hermanos/',BFamilia_hermanos, name="BFamilia_hermanos" ),
    path('BFamilia_primos/',BFamilia_primos, name="BFamilia_primos" ),
    path('BFamilia_lugar/',BFamilia_lugar, name="BFamilia_lugar" ),
    path('BFamilia_trabajan/',BFamilia_trabajan, name="BFamilia_trabajan" ),
    path('Bhermanos/',Bhermanos, name="Bhermanos"),
    path('Bprimos/',Bprimos, name="Bprimos"),
    path('Blugar/',Blugar, name="Blugar"),
    path('Btrabajan/',Btrabajan, name="Btrabajan"),
    path('leerTios',leerTios, name="leerTios"),
    path('eliminarTios/<id>',eliminarTios, name="eliminarTios"),
    path('editarTios/<id>',editarTios, name="editarTios"),
    path('',Inicio, name="inicio"),
    
    path('Hermanos/Lista/',HermanosLista.as_view(), name="HermanosLista"),
    path('Hermanos/Crear/',HermanosCrear.as_view(), name="HermanosCrear"),
    path('Hermanos/Editar/<pk>',HermanosEditar.as_view(), name="HermanosEditar"),
    path('Hermanos/Borrar/<pk>',HermanosBorrar.as_view(), name="HermanosBorrar"),
    path('Hermanos/Ver/<pk>',HermanosDetalle.as_view(), name="HermanosDetalle"),

    path('Tios/Lista/',TiosLista.as_view(), name="TiosLista"),
    path('Tios/Crear/',TiosCrear.as_view(), name="TiosCrear"),
    path('Tios/Editar/<pk>',TiosEditar.as_view(), name="TiosEditar"),
    path('Tios/Borrar/<pk>',TiosBorrar.as_view(), name="TiosBorrar"),
    path('Tios/Ver/<pk>',TiosDetalle.as_view(), name="TiosDetalle"),

    path('Primos/Lista/',PrimosLista.as_view(), name="PrimosLista"),
    path('Primos/Crear/',PrimosCrear.as_view(), name="PrimosCrear"),
    path('Primos/Editar/<pk>',PrimosEditar.as_view(), name="PrimosEditar"),
    path('Primos/Borrar/<pk>',PrimosBorrar.as_view(), name="PrimosBorrar"),
    path('Primos/Ver/<pk>',PrimosDetalle.as_view(), name="PrimosDetalle"),

    path('Lugar/Lista/',LugarLista.as_view(), name="LugarLista"),
    path('Lugar/Crear/',LugarCrear.as_view(), name="LugarCrear"),
    path('Lugar/Editar/<pk>',LugarEditar.as_view(), name="LugarEditar"),
    path('Lugar/Borrar/<pk>',LugarBorrar.as_view(), name="LugarBorrar"),
    path('Lugar/Ver/<pk>',LugarDetalle.as_view(), name="LugarDetalle"),

    path('Trabajo/Lista/',TrabajoLista.as_view(), name="TrabajoLista"),
    path('Trabajo/Crear/',TrabajoCrear.as_view(), name="TrabajoCrear"),
    path('Trabajo/Editar/<pk>',TrabajoEditar.as_view(), name="TrabajoEditar"),
    path('Trabajo/Borrar/<pk>',TrabajoBorrar.as_view(), name="TrabajoBorrar"),
    path('Trabajo/Ver/<pk>',TrabajoDetalle.as_view(), name="TrabajoDetalle"),
    #Adminsitración del Login
    path('Admin_login/', Admin_login, name="Admin_login"),
    path('Admin_registro/', Admin_registro, name="Admin_registro"),
    path('Admin_logout/', LogoutView.as_view(), name="Admin_logout"),
    path('Admin_perfil/', Admin_perfil, name="Admin_perfil"),

    path('AgregarAvatar/', AgregarAvatar, name="AgregarAvatar"),

    path('Blog/', blog, name="Blog")

]

