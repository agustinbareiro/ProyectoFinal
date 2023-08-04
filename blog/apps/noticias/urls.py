from django.urls import path
from . import views
# from .views import ModificarComentario

app_name = 'noticias'

#URLS de app Noticias
urlpatterns = [
    path('', views.inicio, name='inicio'),

    #url para el detalle de la noticia por pk
    path('<int:pk>', views.Detalle_Noticias, name="detalle"),

    #url COMENTARIO
    path('comentario', views.Comentario_Noticia, name='comentar'),
    # path('comentario/new/', views.ComentarioCreateView, name='comentar'),

    #url Borrar comentario
    path('borrar_comentario/<int:comentario_id>/', views.borrar_comentario, name='borrar_comentario'),

    # path('editar_comentario/<int:pk>/', ModificarComentario.as_view(), name='editar_comentario'),

    # path('comentario', views.AgregarComentarioView.as_view(), name='agregar_comentario'),
    # # path('comentario/<int:pk>/editar/', views.EditarComentarioView.as_view(), name='editar_comentario'),
    # path('comentario/<int:pk>/borrar/', views.BorrarComentarioView.as_view(), name='borrar_comentario'),

    #url Editar comentario
    # path('comentario/<int:pk>/editar/', views.ComentarioUpdateView.as_view(), name='editar_comentario'),
]