from django.db import models
from django.contrib.auth.models import User


class Receta(models.Model):
    
    
    nombre = models.CharField(max_length=100, help_text="Nombre de la receta")
    ingredientes = models.TextField(max_length=1000, help_text="Ingredientes",)
    pasos = models.TextField(max_length=2000, help_text="pasos a seguir en la receta")
    prioridad = models.CharField(
        max_length=20,
        blank=True,
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre