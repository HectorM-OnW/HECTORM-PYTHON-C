from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
import json

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum, Max, Avg

from .models import Reportes
from .forms import ReportesForm

from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm

# Create your views here.
def index(request):

    return HttpResponse("Gobierno responde a tus solicitudes!")

class Consultar(View):
    template_name = 'consultar.html'

    def post(self, request, ):

        return render(request, self.template_name)
    
    @method_decorator(login_required)
    def get(self, request):
        reportes = Reportes.objects.all()

        return render(request, self.template_name, {'reportes': reportes})
    
class Crear(View):
    template_name = 'crear.html'
    def post(self, request, ):
        form = ReportesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultar')

        return render(request, self.template_name, {'form': form})
    

    def get(self, request):
        form = ReportesForm()
        return render(request, self.template_name, {'form': form})
    
class EliminarReporte(View):
    def post(self, request, reporte_id):    
        reporte = get_object_or_404(Reportes, pk=reporte_id)
        reporte.delete()
        return redirect('consultar')          

@login_required 
def estadisticas_reportes(request):
    # Obtener el número total de edad de los ciudadanos
    total_edad = Reportes.objects.aggregate(total_edad=Sum('edad'))['total_edad']

    # Obtener la edad máxima de los ciudadanos
    max_edad = Reportes.objects.aggregate(max_edad=Max('edad'))['max_edad']

    # Obtener el número promedio de edad de los ciudadanos
    promedio_edad = Reportes.objects.aggregate(promedio_edad=Avg('edad'))['promedio_edad']

    return render(request, 'estadisticas/estadisticas_reportes.html',{
        'total_edad': total_edad,
        'max_edad': max_edad,
        'promedio_edad': promedio_edad
    })

def register(request):
    # Verificar si la solicitud es del tipo POST (envío de datos del formulario)
    if request.method == 'POST':
        # Crear una instancia del formulario de registro (con los datos enviados en la solicitud)
        form = UserRegistrationForm(request.POST)
        # Verificar si el formulario es válido (todos los campos requeridos están completos y las validaciones pasaron)
        if form.is_valid():
            # Guardar los datos del formulario en la base de datos (crear un nuevo usuario)
            form.save()
            # Obtener el nombre de usuario ingresado en el formulario
            username = form.cleaned_data.get('username')
            # Obtener la contraseña ingresada en el formulario (la contraseña ya está hasheada)
            password = form.cleaned_data.get('password1')
            # Autenticar al nuevo usuario recién registrado
            user = authenticate(username=username, password=password)
            # Iniciar sesión del usuario en la sesión actual
            login(request, user)
            # Redireccionar al usuario a la página de inicio (insertar el nombre de la URL que deseas dirigir)
            return redirect('login')
    else:
        # Si la solicitud no es del tipo POST, crear una instancia de formulario en blanco
        form = UserRegistrationForm()
    # Renderizar la plantilla de registro con el formulario (ya sea en blanco o con datos ingresados previamente)
    return render(request, 'registration/register.html', {'form': form})