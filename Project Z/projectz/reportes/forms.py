# Imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Reportes

# Classes
class ReportesForm(forms.ModelForm):
    class Meta:
        model = Reportes
        fields = ['titulo', 'accion', 'categoria', 'estado', 'ciudad', 'cp', 'edad', 'descripcion']

    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo')
        accion = cleaned_data.get('accion')
        categoria = cleaned_data.get('categoria')
        estado = cleaned_data.get('estado')
        ciudad = cleaned_data.get('ciudad')
        cp = cleaned_data.get('cp')
        edad = cleaned_data.get('edad')
        descripcion = cleaned_data.get('descripcion')

        if not titulo or not accion or not categoria or not estado or not ciudad or not cp or not edad or not descripcion:
            raise forms.ValidationError('Por favor completa todos los campos')
        
        return cleaned_data
    
class UserRegistrationForm(UserCreationForm):
    # Agregar un campo adicional para el correo electrónico (EmailField)
    email = forms.EmailField()

    class Meta:
        # Especificar el modelo con el que está relacionado el formulario (User en este caso)
        model = User
        # Especificar los campos que se mostrarán en el formulario y en qué orden
        fields = ['username','email','password1','password2']