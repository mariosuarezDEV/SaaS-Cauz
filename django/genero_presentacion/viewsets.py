from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .models import ModelGeneroEventos
from .serializers import SerializerGeneroEventos

class ViewSetGeneroEventos(viewsets.ModelViewSet):
    queryset = ModelGeneroEventos.objects.all()
    serializer_class = SerializerGeneroEventos
    
    def get_permissions(self):
        if self.action == "list": # Mandar a trer la accion que se esta ejecutando (Metodo HTPP)
            # ist -> Get
            # create -> Post
            return [AllowAny()]
        return [IsAuthenticated()]