from django.shortcuts import render, HttpResponse
from apps.noticias.models import Noticia
from django.db.models import Q 

# Create your views here.

def home(request):
    queryset = request.GET.get("search")    
    noti = {}
    if queryset:
        v = Noticia.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(cuerpo__icontains = queryset)
         ).distinct()        
        noti['noticias'] = v        
    return render(request, 'index.html', noti)
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