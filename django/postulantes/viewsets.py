from rest_framework import viewsets

# from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
# Importar el modelo
from .models import ModelPostulante
# Importar el serializador
from .serializers import PostulanteSerializer

# Crear la clase PostulanteViewSet
class PostulanteViewSet(viewsets.ModelViewSet):
    queryset = ModelPostulante.objects.all()
    serializer_class = PostulanteSerializer
    permission_classes = [IsAuthenticated]