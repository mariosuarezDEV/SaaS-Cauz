from rest_framework import routers
from django.urls import path

from .viewsets import ViewSetSolicitudEventos

router = routers.DefaultRouter()
router.register(r'solicitud', ViewSetSolicitudEventos)

urlpatterns = router.urls