from django.db import models

class Edificio(models.Model):
    id = models.AutoField(primary_key=True)
    edificio = models.TextField()
    escala = models.DecimalField(max_digits=10, decimal_places=2)
    materiales = models.TextField()
    construccion = models.PositiveIntegerField(help_text="Año de construcción")
    proposito = models.TextField()
    ubicacion = models.TextField()
    nivel = models.TextField()

    def __str__(self):
        return self.edificio  
