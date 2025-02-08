from rest_framework import serializers
from .models import ModelPresentaciones, ModelIntegrantes

class PresentacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPresentaciones
        fields = '__all__'
        
class IntegrantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelIntegrantes
        fields = '__all__'
        