from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "bcr_silva.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import bcr_silva.users.signals  # noqa F401
        except ImportError:
            pass
