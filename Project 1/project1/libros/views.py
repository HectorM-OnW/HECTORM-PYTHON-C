from django.http import HttpResponse 
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
import json

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum, Max, Avg

from .models import Libros
from .forms import LibroForm

def index(request):

    return HttpResponse("Hola Mundo")


class Inicio(View):
    template_name = 'inicio.html'

    def post(self, request):

        return render(request, self.template_name)
    
    @method_decorator(login_required)
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

def estadisticas_libros(request):
    # Obtener el número total de páginas de todos los libros
    total_paginas = Libros.objects.aggregate(total_paginas=Sum('pagina'))['total_paginas']

    # Obtener el año máximo de publicación
    max_anio_publicacion = Libros.objects.aggregate(max_anio_publicacion=Max('año_de_publicacion'))['max_anio_publicacion']

    # Obtener el número promedio de páginas de todos los libros
    promedio_paginas = Libros.objects.aggregate(promedio_paginas=Avg('pagina'))['promedio_paginas']

    return render(request, 'estadisticas/estadisticas_libros.html',{
        'total_paginas': total_paginas,
        'max_anio_publicacion': max_anio_publicacion,
        'promedio_paginas': promedio_paginas
    })
    


    
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

