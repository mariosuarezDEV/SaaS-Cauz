from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from .models import ModelPresentaciones, ModelIntegrantes

from .serializers import PresentacionesSerializer, IntegrantesSerializer

class PresentacionesViewSet(viewsets.ModelViewSet):
    queryset = ModelPresentaciones.objects.all()
    serializer_class = PresentacionesSerializer
    permission_classes = [IsAuthenticated]
    
class IntegrantesViewSet(viewsets.ModelViewSet):
    queryset = ModelIntegrantes.objects.all()
    serializer_class = IntegrantesSerializer
    permission_classes = [IsAuthenticated]
    