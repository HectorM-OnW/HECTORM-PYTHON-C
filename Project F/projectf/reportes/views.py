from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect
import json

from .models import CrearReporte

# Create your views here.
def index(request):

    return HttpResponse("Hola Mundo")

class Crear(View):
    template_name = 'crear.html'

    def post():

        return
    

    def get(self, request):
        
        print('Ya inició el GET--------------**')
        return render(request, self.template_name)
    
def crear_reporte(request):
    nuevo_reporte = CrearReporte(
        titulo = "Calle dañada, av. Ortiz Mena",
        accion = "Reporte de problema",
        categoria = "Vial",
        descripcion = "Hay dos baches en la avenida Ortiz Mena casi llegando a Américas muy grandes que necesitan reparación inmediatamente",
        estado = "Chihuahua",
        ciudad = "Chihuahua",
        cp = 31110
    )
    nuevo_reporte.save()

    return HttpResponse('Reporte subido correctamente')