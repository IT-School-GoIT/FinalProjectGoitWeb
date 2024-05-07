from django.apps import AppConfig


class S3StorageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "s3_storage"
    path = "/app/s3_storage"


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "s3_storage"

    def ready(self):
        import users.signals  # noqa
