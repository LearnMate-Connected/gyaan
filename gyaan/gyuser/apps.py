from django.apps import AppConfig


class GyuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gyuser'
    verbose_name = 'User Management'

    def ready(self):
        import gyuser.signals