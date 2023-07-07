from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('inicio', views.Inicio.as_view(), name='inicio'),
    #path('insertar', views.insertar_libro, name='insertar'),
    path('formulario', views.Formulario.as_view(), name='formulario')
]