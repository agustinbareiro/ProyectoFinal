from django.shortcuts import render, redirect
from .models import Noticia, Categoria, Comentario
from django.urls import reverse_lazy
from django.db.models import Q

#decorador para ver las noticias solamente como usuario logueado
from django.contrib.auth.decorators import login_required

def inicio(request):
    # ctx = {}
    # clase.objects.all()==> select * from noticia
    # noticia = Noticia.objects.all()
    # ctx["noticias"] = noticia
    # return render(request, 'noticias/inicio.html', ctx)
    contexto={}
    id_categoria = request.GET.get('id', None)

    if id_categoria:
        v = Noticia.objects.filter(categoria_noticias = id_categoria)
    else:
        v = Noticia.objects.all() #una lista

    contexto['noticias'] = v

    cat = Categoria.objects.all().order_by('nombre')
    contexto['categorias'] = cat

    return render(request, 'noticias/inicio.html', contexto)

# ClaseName.objects.all()             select * from noticias
# ClaseName.objects.get(pk = 1)       select * from noticias where id = 1
# ClaseName.objects.filter(categoria) select * from noticias where categorias = reviews

@login_required
def Detalle_Noticias(request, pk):
    contexto = {}
    n = Noticia.objects.get(pk=pk)
    contexto['noticia'] = n

    c = Comentario.objects.filter(noticia=n)
    contexto['comentarios'] = c

    return render(request,'noticias/detail.html', contexto)


    

@login_required
def Comentario_Noticia(request):
    comentario = request.POST.get('comentario', None)
    user = request.user
    noti = request.POST.get('id_noticia', None)
    noticia = Noticia.objects.get(pk = noti)
    coment = Comentario.objects.create(usuario= user, noticia= noticia, texto=comentario)

    return redirect(reverse_lazy('noticias:detalle',kwargs={"pk":noti}))