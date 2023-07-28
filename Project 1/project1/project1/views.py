from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout

def custom_logout(request):
    logout(request)
    return redirect('/libros/inicio')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect()
        else:
            messages.error(request, 'Crendenciales Inválidas')
            return render(request, login.html)

    return redirect()