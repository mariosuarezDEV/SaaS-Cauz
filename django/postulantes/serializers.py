from rest_framework import serializers
from .models import ModelPostulante

class PostulanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPostulante
        fields = [
            'id',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'correo',
            'telefono',
            'calle',
            'numero',
            'colonia',
            'cp',
            'municipio',
            'estado',
            'pais',
        ]
        
        # Validar informacion
        def validate(self, data):
            if not data['nombre']:
                raise serializers.ValidationError('El nombre es requerido.')
            if not data['apellido_paterno']:
                raise serializers.ValidationError('El apellido paterno es requerido.')
            if not data['apellido_materno']:
                raise serializers.ValidationError('El apellido materno es requerido.')
            if not data['correo']:
                raise serializers.ValidationError('El correo es requerido.')
            if not data['telefono']:
                raise serializers.ValidationError('El telefono es requerido.')
            return data