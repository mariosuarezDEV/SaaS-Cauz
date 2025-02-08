from django.db.models.signals import post_save # Enviar señales después de guardar
from django.dispatch import receiver # Recibir señales

from .models import ModelPostulante

# 