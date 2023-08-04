from django.contrib import admin
from .models import Usuario, Contacto

# Register your models here.
admin.site.register(Contacto)
admin.site.register(Usuario)