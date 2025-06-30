from django.db import models

class Museo(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre