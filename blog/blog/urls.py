"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #importamos include para poder trabajar con las urls de noticias
# from apps.noticias import views
from . import views
# url de login
from django.contrib.auth import views as auth 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('', views.inicio, name='home'),
    path('admin/', admin.site.urls),
    # path para la URL de la vista de home
    path('', views.home, name='index'),
    # path para la URL de sobre nosotros
    path('about', views.about, name='about'),
    # # path para la URL de sobre ayuda
    # path('help', views.help, name='help'),

    # path('', views.busqueda, name='index'),

    #path URL APP NOTICIA
    path('news/', include('apps.noticias.urls')),

    # URL LOGIN
    path('login/', auth.LoginView.as_view(template_name= 'usuarios/login.html'), name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),

    # Registro
    path('users/', include('apps.usuarios.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)