from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .models import ModelSolicitudEventos
from .serializers import SerializerSolicitudEventos

class ViewSetSolicitudEventos(viewsets.ModelViewSet):
    queryset = ModelSolicitudEventos.objects.all()
    serializer_class = SerializerSolicitudEventos
    permission_classes = [IsAuthenticated]
    # Acciones personalizadas