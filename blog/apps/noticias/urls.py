from django.urls import path
from . import views

app_name = 'noticias'

#URLS de app Noticias
urlpatterns = [
    path('', views.inicio, name='inicio'),
]