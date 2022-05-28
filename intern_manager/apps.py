from django.apps import AppConfig
from django.db.models.signals import post_save


class InternManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'intern_manager'

    def ready(self):
        import intern_manager.signals
