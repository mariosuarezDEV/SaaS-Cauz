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
        read_only_fields = ['id', 'fecha_solicitud', 'fecha_actualizacion']
    # Validar que material sea una URL
    def validate_meterial(self, value):
        if 'http' not in value:
            raise serializers.ValidationError('El material debe ser una URL')
        return value