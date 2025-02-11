from django.urls import path
from rest_framework import routers

from .viewsets import PresentacionesViewSet, IntegrantesViewSet

router = routers.DefaultRouter()
router.register('presentaciones', PresentacionesViewSet)
router.register('integrantes', IntegrantesViewSet)

urlpatterns = router.urls
