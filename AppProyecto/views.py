from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import HttpResponse
from AppProyecto.forms import Formulario_cliente, Formulario_vendedor, Formulario_articulo
from AppProyecto.models import Cliente, Vendedor, Articulo
from templates import *

from typing import List

from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppProyecto.models import Curso, Profesor, Avatar
from AppProyecto.forms import CursoFormulario, ProfesorFormulario, UserRegisterForm,UserEditForm,AvatarFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

#Para la prueba unitaria
import string



#Decorador por defecto
from django.contrib.auth.decorators import login_required

from django.views.generic.base import TemplateView

def navvar(request):
    return render(request, "AppProyecto/navvar.html")
def blog1(request):
    return render(request, "AppProyecto/blog1.html")
def about(request):
    return render(request, "AppProyecto/about.html")
def pages(request):
    return render(request, "AppProyecto/pages.html")


def inicio(request):
    return render(request, "AppProyecto/inicio.html")

def home_vendedores(request):
    diccionario = {}
    plantilla = loader.get_template("AppProyecto/home_vendedores.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def home_articulos(request):
    diccionario = {}
    plantilla = loader.get_template("AppProyecto/home_articulos.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def home_clientes(request):
    diccionario = {}
    plantilla = loader.get_template("AppProyecto/home_clientes.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def form_clientes(request):
    if (request.method == "POST"):
        formulario = Formulario_cliente(request.POST)
        if (formulario.is_valid()):
            info = formulario.cleaned_data
            nombre1 = info.get("nombre")
            apellido1 = info.get("apellido")
            nro_telefono1 = info.get("nro_telefono")
            dni1 = info.get("dni")
            nro_cliente1 = info.get("nro_cliente")
            cliente = Cliente(nombre = nombre1, apellido = apellido1, nro_telefono = nro_telefono1, dni = dni1, nro_cliente = nro_cliente1)
            cliente.save()
            return (render(request, "AppProyecto/inicio.html", {"mensaje": "Cliente creado"}))
        else:
            return (render(request, "AppProyecto/inicio.html", {"mensaje": "Error"}))
        
    else:
        formulario = Formulario_cliente()
        return (render(request, "form_clientes.html", {"formulario": formulario}))

def form_vendedores(request):
    if (request.method == "POST"):
        formulario = Formulario_vendedor(request.POST)
        if (formulario.is_valid()):
            info = formulario.cleaned_data
            nombre1 = info.get("nombre")
            apellido1 = info.get("apellido")
            nro_telefono1 = info.get("nro_telefono")
            dni1 = info.get("dni")
            cuit1 = info.get("cuit")
            vendedor = Vendedor(nombre = nombre1, apellido = apellido1, nro_telefono = nro_telefono1, dni = dni1, cuit = cuit1)
            vendedor.save()
            return (render(request, "AppProyecto/inicio.html", {"mensaje": "Vendedor creado"}))
        else:
            return (render(request, "AppProyecto/inicio.html", {"mensaje": "Error"}))
        
    else:
        formulario = Formulario_vendedor()
        return (render(request, "AppProyecto/form_vendedores.html", {"formulario": formulario}))

def form_articulos(request):
    if (request.method == "POST"):
        formulario = Formulario_articulo(request.POST)
        if (formulario.is_valid()):
            info = formulario.cleaned_data
            nombre1 = info.get("nombre")
            categoria1 = info.get("categoria")
            descripcion1 = info.get("descripcion")
            precio1 = info.get("precio")
            articulo = Articulo(nombre = nombre1, categoria = categoria1, descripcion = descripcion1, precio = precio1)
            articulo.save()
            return (render(request, "AppProyecto/inicio.html", {"mensaje": "Articulo creado"}))
        else:
            return (render(request, "AppProyecto/inicio.html", {"mensaje": "Error"}))
        
    else:
        formulario = Formulario_articulo()
        return (render(request, "AppProyecto/form_articulos.html", {"formulario": formulario}))

def busqueda_cliente(request):
    return (render(request, "AppProyecto/busqueda_cliente.html"))

def resultado_clientes(request):
    if (request.GET.get("nro_cliente")):
        nro_cliente = request.GET.get("nro_cliente")
        clientes = Cliente.objects.filter(nro_cliente = nro_cliente)
        if (len(clientes) != 0):
            return (render(request, "AppProyecto/resultados_clientes.html", {"clientes": clientes}))
        else:
            return render(request, "AppProyecto/resultados_clientes.html", {"mensaje": "Cliente(s) no encontrado(s)"})
    else:
        return (render(request, "AppProyecto/busqueda_cliente.html", {"mensaje": "Por favor, ingrese un numero de cliente"}))

def busqueda_vendedor(request):
    return (render(request, "AppProyecto/busqueda_vendedor.html"))

def resultado_vendedores(request):
    if (request.GET.get("cuit")):
        cuit1 = request.GET.get("cuit")
        vendedores = Vendedor.objects.filter(cuit = cuit1)
        if (len(vendedores) != 0):
            return (render(request, "AppProyecto/resultados_vendedores.html", {"vendedores": vendedores}))
        else:
            return render(request, "AppProyecto/resultados_vendedores.html", {"mensaje": "Vendedor(es) no encontrado(s)"})
    else:
        return (render(request, "AppProyecto/busqueda_vendedor.html", {"mensaje": "Por favor, ingrese un numero de CUIT del vendedor"}))

def busqueda_articulo(request):
    return (render(request, "AppProyecto/busqueda_articulo.html"))

def resultado_articulos(request):
    if (request.GET.get("categoria")):
        categoria = request.GET.get("categoria")
        articulos = Articulo.objects.filter(categoria = categoria)
        if (len(articulos) != 0):
            return (render(request, "AppProyecto/resultados_articulos.html", {"articulos": articulos}))
        else:
            return render(request, "AppProyecto/resultados_articulos.html", {"mensaje": "Articulo(s) no encontrado(s)"})
    else:
        return (render(request, "AppProyecto/busqueda_articulo.html", {"mensaje": "Por favor, ingrese una categoria de Articulo"}))
    
    
def logout_request(request):
      logout(request)
     
      return redirect("inicio")
     

def login(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"AppProyecto/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"AppProyecto/inicio.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"AppProyecto/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"AppProyecto/login.html", {'form':form} )



def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppProyecto/inicio.html" ,  {"mensaje":"Usuario Creado :)"})


      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppProyecto/register.html" ,  {"form":form})



@login_required
def editarPerfil(request):

      #Instancia del login
      usuario = request.user
     
      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
            
                  #Datos que se modificarán
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password1']
                  usuario.save()

                  return render(request, "AppProyecto/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UserEditForm(initial={ 'email':usuario.email}) 

      #Voy al html que me permite editar
      return render(request, "AppProyecto/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})



@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html

            if miFormulario.is_valid:   #Si pasó la validación de Django


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "AppProyecto/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

      return render(request, "AppProyecto/agregarAvatar.html", {"miFormulario":miFormulario})


def urlImagen():

      return "/media/avatares/logo.png"