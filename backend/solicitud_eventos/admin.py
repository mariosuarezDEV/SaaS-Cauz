from django.contrib import admin

# Register your models here.
from .models import ModelSolicitudEventos

admin.site.register(ModelSolicitudEventos) # Registrar el modelo SolicitudEventos en el admin