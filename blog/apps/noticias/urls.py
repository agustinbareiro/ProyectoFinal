from django.urls import path
from . import views
app_name = 'noticias'

#URLS de app Noticias
urlpatterns = [
    path('', views.inicio, name='inicio'),

    #url para el detalle de la noticia por pk
    path('<int:pk>', views.Detalle_Noticias, name="detalle"),

    #url COMENTARIO
    path('comentario', views.Comentario_Noticia, name='comentar'),
]