from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'message': '¡Bienvenido al Proyecto Educativo!'})
