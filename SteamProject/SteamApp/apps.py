from django.apps import AppConfig

class SteamappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SteamProject.SteamApp'

    def ready(self):
        import SteamProject.SteamApp.signals