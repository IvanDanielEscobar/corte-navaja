from django.db import models

class Corte(models.Model):
    name = models.CharField(max_length=100)
    precio =models.IntegerField()
    descripcion =models.TextField(max_length=250)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    corte = models.ForeignKey(Corte, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.nombre}'