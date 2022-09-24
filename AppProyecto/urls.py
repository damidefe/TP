from django.urls import path
from AppProyecto.views import *
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path("", inicio,name = 'inicio'),
    path('about/', about, name = 'about'),
    path('blog1/', about, name = 'blog1'),
    path('pages/', pages, name = 'pages'),
    path('navvar/', navvar, name = 'navvar'),
    
    path('login/', login, name = 'login'),
    path('register/', register, name = 'register'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name = 'logout'),

    path('home_clientes/', home_clientes, name = 'home_clientes'),
    path('form_clientes/', form_clientes, name = 'form_clientes'),
    path('busqueda_cliente/', busqueda_cliente, name = 'busqueda_cliente'),
    path('resultado_clientes/', resultado_clientes, name = 'resultado_clientes'),

    path('home_vendedores/', home_vendedores, name = 'home_vendedores'),
    path('form_vendedores/', form_vendedores, name = 'form_vendedores'),
    path('busqueda_vendedor/', busqueda_vendedor, name = 'busqueda_vendedor'),
    path('resultado_vendedores/', resultado_vendedores, name = 'resultado_vendedores'),

    path('home_articulos/', home_articulos, name = 'home_articulos'),
    path('form_articulos/', form_articulos, name = 'form_articulos'),
    path('busqueda_articulo/', busqueda_articulo, name = 'busqueda_articulo'),
]