from django.db import models

# Create your models here.
class Libros(models.Model):

    class Meta:
        verbose_name = "Libros"
        verbose_name_plural = "Libros"

    titulo = models.CharField("Título", max_length=300, default="Sin Nombrar")
    edicion = models.CharField("Edición", max_length=300, default="Sin Especificar")
    editorial = models.CharField("Editorial", max_length=300, default="Sin Especificar")
    año_de_publicacion = models.IntegerField("Año de publicación", default=200)
    pagina = models.IntegerField("Número de páginas", blank=False)

    def _str_(self):
        return self.titulo
    
    
    '''
    En caso de intentar retornar algun dato alfanumérico hay que conovertirlo a string, por ejemplo...
    '''
       # return str(self.año_de_publicacion)