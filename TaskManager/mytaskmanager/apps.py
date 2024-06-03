from django.apps import AppConfig

class MytaskmanagerConfig(AppConfig):
    """
    configuration class for 'mytaskmanager' Django app.

    this class provides configuration for 'mytaskmanager' app,
    including specifying default auto field and name of app.
    """
    default_auto_field = 'django.db.models.BigAutoField'  # Specifies default auto field for models in app
    name = 'mytaskmanager'  # Specifies name of Django app
