from django.db import models
from Aplicaciones.Museos.models import Museo
from Aplicaciones.Disenadores.models import DisenadorUX

class ModuloInteractivo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

    # Relaciones con otras tablas
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE)
    disenador = models.ForeignKey(DisenadorUX, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo
