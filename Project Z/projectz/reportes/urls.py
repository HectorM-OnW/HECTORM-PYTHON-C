
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('consultar/', views.Consultar.as_view(), name='consultar'),
    path('crear/', views.Crear.as_view(), name='crear'),
    path('eliminar-reporte/<int:reporte_id>/', views.EliminarReporte.as_view(), name='eliminar_reporte'),
    path('estadisticas/', views.estadisticas_reportes, name='estadisticas_reportes'),
    path('register/', views.register, name='register')
]

'''
1.Con la función path primero se define el nombre como aparecerá en la URL, si no tiene entonces será la default.
2.Luego le decimos, ve a mi archivo views y trae index y finalmente definimos el nombre de retorno de la función.

path('', views.index, name='index') >>> Esta estructura es porque estamos llamando desde una función, no desde una clase.

path('consultar', views.Consultar.as_view(), name='consultar') >>> Aquí tenemos que incluir as_view(), porque se esta llamando desde una clase.


'''