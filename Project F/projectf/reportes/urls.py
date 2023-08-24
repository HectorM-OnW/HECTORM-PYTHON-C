
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear', views.Crear.as_view(), name='crear'),
    path('crear-reporte/', views.crear_reporte, name='crear_reporte')
]

'''
1.Con la función path primero se define el nombre como aparecerá en la URL, si no tiene entonces será la default.
2.Luego le decimos, de a mi archivo views y trae index y finalmente definimos el nombre de retorno de la función

path('', views.index, name='index') >>> Esta será la estructura ya que estamos llamando desde una función no desde una clase

path('crear', views.Crear.as_view(), name='crear') >>> Aquí tenemos que incluir as_view() porque se esta llamando desde una clase


'''