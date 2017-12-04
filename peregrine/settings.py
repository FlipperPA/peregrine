from django.conf import settings

from .models import Settings


def get_setting(key, default):
    """
    Returns a value for key from the Settings model.
    """
    setting = Settings.objects.get(key=key)


def get_clear_cache():
    """
    Default to clearing the cache after each page edit.
    """

    return getattr(settings, "WP_CLEAR_CACHE", False)
