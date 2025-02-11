from rest_framework  import serializers

from .models import ModelGeneroEventos

class SerializerGeneroEventos(serializers.ModelSerializer):
    class Meta:
        model = ModelGeneroEventos
        fields = [
            'id',
            'nombre',
            'descricion',
            'fecha_creacion',
            'fecha_modificacion',
            'usuario_modificacion',
        ]
        read_only_fields= ['id', 'fecha_creacion', 'fecha_modificacion']
        