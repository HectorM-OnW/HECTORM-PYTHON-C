from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect
import json

from .models import Productos_Minimos
from .forms import ProductosForm
# Create your views here.

def index(request):

    return HttpResponse("Hola Mundo")


class Productos(View):
    template_name = 'productos.html'


    def post(self, request):
        form = ProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')

        return render(request, self.template_name, {'form': form})



    def get(self, request):
        productos = Productos_Minimos.objects.all()
        form = ProductosForm()
        return render(request, self.template_name, {'form': form, 'productos': productos })
    