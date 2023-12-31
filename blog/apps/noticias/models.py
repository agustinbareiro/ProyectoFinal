from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=150)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to= 'noticias')
    categoria_noticias = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titulo

class Comentario(models.Model):
    texto= models.TextField(null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    noticia = models.ForeignKey(Noticia, on_delete= models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return f"{self.noticia}{self.texto}"