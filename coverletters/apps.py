from django.apps import AppConfig


class CoverlettersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coverletters'

    def ready(self):
        pass
        # from . import signals
