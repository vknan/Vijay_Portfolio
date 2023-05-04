from django.apps import AppConfig


class MyAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "myapp"

    # def ready(self):
    #     try:
    #         import myapp.signals
    #     except AppRegistryNotReady:
    #         pass




    
