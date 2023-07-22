from django.shortcuts import render, HttpResponse
from .models import Noticia

# Create your views here.
def inicio(request):
    ctx = {}
    # clase.objects.all()==> select * from noticia
    noticia = Noticia.objects.all()
    ctx["noticias"] = noticia
    return render(request, 'noticias/inicio.html', ctx)

# ClaseName.objects.all()             select * from noticias
# ClaseName.objects.get(pk = 1)       select * from noticias where id = 1
# ClaseName.objects.filter(categoria) select * from noticias where categorias = reviews