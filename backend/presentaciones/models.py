from django.db import models

# Create your models here.

class ModelIntegrantes(models.Model):
    #Informacion
    nombre = models.CharField(max_length=50, blank=False, null=False, verbose_name="Nombre(s) del integrante")
    apellidos = models.CharField(max_length=50, blank=True, null=True, verbose_name="Apellidos del integrante")
    dieta = models.CharField (max_length=100, blank=True, null=True, verbose_name="Especificacion de dieta", default="Sin especificación")
    
    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
    
    class Meta:
        verbose_name = 'Integrante'
        verbose_name_plural = 'Integrantes'
        db_table = 'integrantes'


class ModelPresentaciones(models.Model):
    #Información
    marca_temporal = models.DateField(blank=True, null=True, verbose_name="Fecha temporal")
    nombre_agrupacion = models.CharField(max_length=100, null=False,blank=False, verbose_name="Nombre de la agrupacion")
    presentacion_grupo = models.CharField(max_length=200, null=False, blank=False,verbose_name="Semblanza del grupo")
    #fotografias =
    #video = 
    # Tiene muchos integrantes
    integrantes = models.ManyToManyField(ModelIntegrantes, verbose_name="Integrantes",null=True, blank=True, related_name="integrantes")
    
    def __str__(self):
        return self.nombre_agrupacion
    class Meta:
        verbose_name = 'Presentacion'
        verbose_name_plural = 'Presentaciones'
        db_table = 'presentaciones'