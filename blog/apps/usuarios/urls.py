from django.urls import path
from . import views

app_name = 'usuarios'

#URLS de app Usuarios
urlpatterns = [
    path('register/', views.Registro.as_view(), name='register'),
]