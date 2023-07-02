from django.db import models

# Create your models here.
class Productos_Minimos(models.Model):
    class Meta:
        verbose_name = "Productos"
        verbose_name_plural = "Productos"
    
    nombre = models.CharField("Nombre", max_length=300, default="N/A")
    descripcion = models.CharField("Descripción", max_length=300, default="N/A")
    precio = models.IntegerField("Precio", default=0)
    fecha_registro = models.CharField("Fecha de registro", max_length=300, default="N/A")
    estatus = models.CharField("Estatus", max_length=300, default="N/A")

    def _str_(self):
        return self.nombre
    