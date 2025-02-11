from django.db import models

# Creación de modelos.

ESTADO_CIVIL = (
    ('soltero', 'Soltero'),
    ('casado', 'Casado'),
    ('divorciado', 'Divorciado'),
    ('viudo', 'Viudo')
)

GENERO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro')
)

class ModelPostulante(models.Model):
    # Informacion
    nombre = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre(s)')
    apellido_paterno = models.CharField(max_length=50, null=False, blank=False, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=50, null=False, blank=False, verbose_name='Apellido Materno')
    fecha_nacimiento = models.DateField(null=True, blank=True)
    # Contacto
    correo = models.EmailField(verbose_name='Correo Electrónico', null=False, blank=False)
    telefono = models.CharField(max_length=10, verbose_name='Teléfono', null=False, blank=False)
    # Ubicación
    calle = models.CharField(max_length=50, null=True, blank=True, verbose_name='Calle')
    numero = models.CharField(max_length=10, null=True, blank=True, verbose_name='Número')
    colonia = models.CharField(max_length=50, null=True, blank=True, verbose_name='Colonia')
    cp = models.CharField(max_length=5, null=True, blank=True, verbose_name='Código Postal')
    municipio = models.CharField(max_length=50, null=True, blank=True, verbose_name='Municipio')
    estado = models.CharField(max_length=50, null=True, blank=True, verbose_name='Estado')
    pais = models.CharField(max_length=50, null=True, blank=True, verbose_name='País')
    # Datos
    genero = models.CharField(max_length=1, choices=GENERO)
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL)
    # foto = models.ImageField(upload_to='postulantes', null=True, blank=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno

    class Meta:
        verbose_name = 'Postulante'
        verbose_name_plural = 'Postulantes'
        db_table = 'postulantes'
        
        