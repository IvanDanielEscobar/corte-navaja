from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UsuarioPersonalizado(AbstractUser):
    nombre_completo = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    dni = models.CharField(max_length=20, null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='users_fp/', null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.dni}"