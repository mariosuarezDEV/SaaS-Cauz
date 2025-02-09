from django.urls import path
from rest_framework import routers

from .viewsets import PostulanteViewSet

router = routers.DefaultRouter()
router.register('postulantes', PostulanteViewSet)

urlpatterns = router.urls