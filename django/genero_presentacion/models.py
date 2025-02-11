from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ModelGeneroEventos(models.Model):
    nombre = models.CharField(max_length=25, null= False, blank= False, verbose_name="Nombre del evento")
    descricion = models.CharField(max_length=50, null= True, blank= True, verbose_name="Breve descripción del evento")
    fecha_creacion = models.DateField(auto_now_add= True, verbose_name="Fecha de creacion del evento")
    fecha_modificacion = models.DateField(auto_now_add= True, verbose_name="Fecha de modificacion del evento")
    usuario_modificacion = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuario Modificacion",  null=False, blank=False)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Genero presentacion'
        verbose_name = 'Genero presentaciones'
        db_table = "generos"