from rest_framework import routers
from django.urls import path

from .viewsets import ViewSetGeneroEventos

router = routers.DefaultRouter()
router.register(r'tipo', ViewSetGeneroEventos)

urlpatterns = router.urls
