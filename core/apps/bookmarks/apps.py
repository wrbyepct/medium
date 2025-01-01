from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BookmarksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.apps.bookmarks"
    verbose_name = _("Bookmarks")
