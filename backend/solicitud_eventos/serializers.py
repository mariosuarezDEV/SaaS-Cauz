from rest_framework import serializers

from .models import ModelSolicitudEventos

class SerializerSolicitudEventos(serializers.ModelSerializer):
    class Meta:
        model = ModelSolicitudEventos
        fields = [
            'id',
            'fecha_solicitud',
            'fecha_actualizacion',
            'nombre_evento',
            'genero',
            'fecha_tentativa',
            'integrantes',
            'meterial',
            'postulante',
        ]
    # Validaciones
    def validate(self, data):
        if data['fecha_tentativa'] < data['fecha_solicitud']:
            raise serializers.ValidationError('La fecha tentativa no puede ser menor a la fecha de solicitud') # Revisar porque no funciona
        return data
    # Validar que material sea una URL
    def validate_meterial(self, value):
        if 'http' not in value:
            raise serializers.ValidationError('El material debe ser una URL')
        return value