from django.contrib import admin

# Register your models here.

from .models import ModelPostulante

class AdminPostulante(admin.ModelAdmin):
    list_display = ['nombre', 'apellido_paterno', 'apellido_materno', 'correo', 'telefono', 'genero', 'estado_civil']
    search_fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'correo', 'telefono']
    list_filter = ['genero', 'estado_civil']
    date_hierarchy = 'fecha_nacimiento'

admin.site.register(ModelPostulante, AdminPostulante)