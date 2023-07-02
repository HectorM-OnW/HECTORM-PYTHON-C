from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

def index(request):

    return HttpResponse("Hola mundo!")

class Inicio(View):
    template_name = 'incio.html'

    def post():

        return
    
    def get(self, request):

        '''
        Esta es mi clase Get
        '''
        print('Ya inició mi GET ------------*')


        return render(request, self.template_name)
    
