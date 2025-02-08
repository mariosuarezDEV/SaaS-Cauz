from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .models import ModelSolicitudEventos
from .serializers import SerializerSolicitudEventos

class ViewSetSolicitudEventos(viewsets.ModelViewSet):
    queryset = ModelSolicitudEventos.objects.all()
    serializer_class = SerializerSolicitudEventos
    
    # Manejador de permisos (Permitir la peticion POST para todos y las demas para usuarios autenticados)
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()] # Cualquier usuario puede hacer una solicitud
        return [IsAuthenticated()] # Solo usuarios autenticados pueden ver, editar o eliminar solicitudes