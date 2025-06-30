from django.db import models

class DisenadorUX(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    experiencia = models.PositiveIntegerField(help_text="Años de experiencia como diseñador UX")

    def __str__(self):
        return self.nombre
