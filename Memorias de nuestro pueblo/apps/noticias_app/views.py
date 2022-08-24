from django.shortcuts import render
from .models import Noticia, Categoria, Comentarios
from django.http.response import Http404
#from django.http import HttpResponse

# Create your views here.
def eventos(request):
    return render(request, 'eventos.html', {})

def index(request):
    texto = {'mensaje_texto': 'Esta es mi primer pagina :)'}
    return render(request, 'index.html', {})

def misionVision(request):
    return render(request, 'mision-vision.html', {})

def noticias(request):
    lista_noticias = Noticia.objects.all().order_by('creado')
    context = {
        "noticias": lista_noticias,
        "MEDIA_ROOT": "media/img/noticias/"
    }
    return render(request, 'noticias.html',context)

def noticiasdetalle(request, id):
    try:
        datanoticia = Noticia.objects.get (id=id)
        lista_comentarios =Comentarios.objects.filter(aprobado=True)

    except Noticia.DoesNotExist :
        raise Http404('La noticia solicitada no existe')

    context = {
        "noticias": datanoticia,
        "comentarios": lista_comentarios
    }
    return render(request, 'noticiasdetalles.html',context)   

def quienesSomos(request):
    return render(request, 'quienes-somos.html', {})

def recursos(request):
    return render(request, 'recursos.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def login(request):
    return render(request, 'login.html', {})