from django.contrib import admin

# Register your models here.
from .models import ModelSolicitudEventos

class AdminSolicitudEventos(admin.ModelAdmin):
    list_display = ['nombre_evento', 'genero', 'fecha_tentativa', 'integrantes', 'meterial', 'postulante', 'estado',]
    search_fields = ['nombre_evento']
    list_filter = ['fecha_solicitud']
    date_hierarchy = 'fecha_solicitud'

admin.site.register(ModelSolicitudEventos, AdminSolicitudEventos)