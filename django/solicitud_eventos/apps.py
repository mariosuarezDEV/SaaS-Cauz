from django.apps import AppConfig


class SolicitudEventosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'solicitud_eventos'
    # Vincular las señales
    def ready(self):
        import solicitud_eventos.signals
