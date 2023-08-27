
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('consultar/', views.Consultar.as_view(), name='consultar'),
    path('crear/', views.Crear.as_view(), name='crear'),
    path('eliminar-reporte/<int:reporte_id>/', views.EliminarReporte.as_view(), name='eliminar_reporte'),
    path('estadisticas/', views.estadisticas_reportes, name='estadisticas_reportes'),
    path('estadisticas-2/', views.estadisticas_reportes_2, name='estadisticas_reportes_2'),
    path('register/', views.register, name='register'),
  
]

'''
path**
1.Con la función path primero se define el nombre como aparecerá en la URL, si no tiene entonces será la default.
2.Luego le decimos, ve a mi archivo views y trae index y finalmente definimos el nombre de retorno de la función.

path('', views.index, name='index') >>> Esta estructura es porque estamos llamando desde una función, no desde una clase.

path('consultar', views.Consultar.as_view(), name='consultar') >>> Aquí tenemos que incluir as_view(), porque se esta llamando desde una clase.

index**
1.La url de index va a mostrar lo que se encuentre dentro de la función index en la carpeta views, 
esta función al no tener HTML vale la pena mencionar que lo que vemos en realidad al ejecutar la url es el HttpResponse.
'''

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)