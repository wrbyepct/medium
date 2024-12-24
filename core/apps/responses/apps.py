from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ResponsesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.apps.responses"
    verbose_name = _("Responses")

    def ready(self):
        import core.apps.responses.signals  # noqa: F401
