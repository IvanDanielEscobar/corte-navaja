from django.db import models

class Corte(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    precio =models.IntegerField()
    descripcion =models.TextField(max_length=250)

    def __str__(self):
        return self.id
