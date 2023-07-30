from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    pass

class Contacto(models.Model):
    nombre = models.CharField(max_length=60)
    correo = models.EmailField()
    asunto = models.CharField(max_length=40)
    texto = models.TextField()

    def __str__(self) -> str:
        return self.nombre
