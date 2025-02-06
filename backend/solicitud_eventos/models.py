from django.db import models
from postulantes.models import ModelPostulante

# Create your models here.

class ModelSolicitudEventos(models.Model):
    # Auditoria
    fecha_solicitud = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de solicitud')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    # Datos de la solicitud
    nombre_evento = models.CharField(max_length=100, verbose_name='Nombre del evento', null=False, blank=False)
    genero = models.CharField(max_length=100, verbose_name='Género', null=True, blank=True)
    fecha_tentativa = models.DateField(verbose_name='Fecha tentativa', null=False, blank=False)
    integrantes = models.CharField(max_length=150 ,verbose_name='Nombre de los integrantes', null=False, blank=False)
    meterial = models.CharField(max_length=500, verbose_name='Material', null=False, blank=False)
    # Relaciones
    postulante = models.ForeignKey(ModelPostulante, on_delete=models.PROTECT, verbose_name='Postulante', null=False, blank=False)
    
    def __str__(self):
        return self.nombre_evento + ' - ' + self.postulante.nombre + ' ' + self.postulante.apellido_paterno + ' ' + self.postulante.apellido_materno
    
    class Meta:
        verbose_name = 'Solicitud de evento'
        verbose_name_plural = 'Solicitudes de eventos'
        ordering = ['fecha_solicitud']
        db_table = 'solicitud_eventos'