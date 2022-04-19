from django.contrib import admin
from . import models



@admin.register(models.Receta)
class Receta(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion',)
    search_fields = ('nombre',)