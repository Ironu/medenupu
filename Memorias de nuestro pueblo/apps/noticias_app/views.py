from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def eventos(request):
    return render(request, 'eventos.html', {})

def index(request):
    texto = {'mensaje_texto': 'Esta es mi primer pagina :)'}
    return render(request, 'index.html', {})

def misionVision(request):
    return render(request, 'mision-vision.html', {})

def noticias(request):
    return render(request, 'noticias.html', {})

def quienesSomos(request):
    return render(request, 'quienes-somos.html', {})

def recursos(request):
    return render(request, 'recursos.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def login(request):
    return render(request, 'login.html', {})