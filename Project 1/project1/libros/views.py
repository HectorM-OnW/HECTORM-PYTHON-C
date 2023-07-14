from django.http import HttpResponse 
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
import json

from .models import Libros
from .forms import LibroForm

def index(request):

    return HttpResponse("Hola Mundo")

class Inicio(View):
    template_name = 'inicio.html'

    def post(self, request):

        return render(request, self.template_name, {'form': form})
    
    def get(self, request):
        libros = Libros.objects.all()
        
        return render(request, self.template_name, {'libros': libros})
    
class Formulario(View):
    template_name = 'formulario.html'
   
    def post(self, request):
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')


        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = LibroForm()
        return render(request, self.template_name, {'form': form})
    
class EliminarLibro(View):
    def post(self, request, libro_id):
        libro = get_object_or_404(Libros, pk=libro_id)
        libro.delete()
        return redirect('inicio')

'''
La siguiente función con Post hacia la base de datos ya no se necesita, porque ya tenemos formulario...

def insertar_libro(request):
    nuevo_libro = Libros ( 
        titulo='El gran libro',
        edicion='Primera Edición',
        editorial='Editorial XYZ',
        año_de_publicacion=2022,
        pagina=200
    )

    nuevo_libro.save()

    return HttpResponse('Libro insertado correctamente')

'''

