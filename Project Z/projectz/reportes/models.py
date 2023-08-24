from django.db import models

# Create your models here.
class Reportes(models.Model):
    class Meta:
        verbose_name = "Reportes"
        verbose_name_plural = "Reportes"

    titulo = models.CharField("Título del reporte", max_length=300, default="Asigna un título para tu reporte o solicitud...")
    accion = models.CharField("Reportar problema/solicitud de información", max_length=300, default="Especifica si es reporte o solicitud...")
    categoria = models.CharField("Categoría", max_length=300, default="Alumbrado, Civil, Vial o Seguridad...")
    estado = models.CharField("Estado", max_length=300, default="Estado de donde se genera el reporte...")
    ciudad = models.CharField("Ciudad", max_length=300, default="Ciudad de donde se genera el reporte...")
    cp = models.IntegerField("Código Postal", default=0)
    edad = models.IntegerField("Edad", default=0)
    descripcion = models.CharField("Descripción", max_length=300, default="Escribe aquí la descripción del problema o solicitud...")

    def _str_(self):
        return self.titulo
    
    
    '''
    _str_  >>> Es un metodo especial en Django que se utiliza para representar una instancia de nuestro modelo 
    como una cadena de texto legible, y no como un código alfanumérico que no nos ayude a identificar que tipo
    de modelo o dato se trata.

    '''

    '''
    En caso de intentar retornar algun dato alfanumérico hay que conovertirlo a string, por ejemplo...
    '''