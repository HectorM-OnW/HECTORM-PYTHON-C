from django import forms
from .models import Libros

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['titulo', 'edicion', 'editorial', 'año_de_publicacion', 'pagina']

    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo')
        edicion = cleaned_data.get('edicion')
        editorial = cleaned_data.get('editorial')
        año_de_publicacion = cleaned_data.get('año_de_publicacion')
        pagina = cleaned_data.get('pagina')

        if not titulo or not edicion or not editorial or not año_de_publicacion or not pagina:
            raise forms.ValidationError('Todos los campos deben estar completos')
        
        return cleaned_data