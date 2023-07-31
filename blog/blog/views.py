from django.shortcuts import render, HttpResponse
from apps.noticias.models import Noticia, Categoria
from django.db.models import Q 

# Create your views here.

def home(request):
    queryset = request.GET.get("search") 
    id_categoria = request.GET.get('id', None)
    order_by = request.GET.get('order_by', 'fecha_desc')   
    contexto = {}
    if queryset:
        v = Noticia.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(cuerpo__icontains = queryset)
         ).distinct().order_by('-titulo')   
        contexto['noticias'] = v        
    elif id_categoria:
        v = Noticia.objects.filter(categoria_noticias = id_categoria)
    elif order_by == 'fecha_asc':
        v = Noticia.objects.order_by('fecha')
    elif order_by == 'fecha_desc':
        v = Noticia.objects.order_by('-fecha')
    elif order_by == 'titulo_asc':
        v = Noticia.objects.order_by('titulo')
    elif order_by == 'titulo_desc':
        v = Noticia.objects.order_by('-titulo')
    else:
        v = Noticia.objects.all().order_by('-titulo') #una lista
    contexto['noticias'] = v
    cat = Categoria.objects.all().order_by('nombre')
    contexto['categorias'] = cat
    return render(request, 'index.html', contexto)
    # else:
    #     ctx = {}
    #     Noticia.objects.all()
    #     # select * from noticia
    #     noticia = Noticia.objects.all()
    #     ctx["noticias"] = noticia
    #     return render(request, 'index.html', ctx)

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')