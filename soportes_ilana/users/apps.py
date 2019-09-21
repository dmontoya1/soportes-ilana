from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "soportes_ilana.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import soportes_ilana.users.signals  # noqa F401
        except ImportError:
            pass
