from rest_framework import viewsets

# from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, AllowAny
# Importar el modelo
from .models import ModelPostulante
# Importar el serializador
from .serializers import PostulanteSerializer

# Crear la clase PostulanteViewSet
class PostulanteViewSet(viewsets.ModelViewSet):
    queryset = ModelPostulante.objects.all()
    serializer_class = PostulanteSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]
        