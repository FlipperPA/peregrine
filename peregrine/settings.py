from django.conf import settings


def get_clear_cache():
    """
    Default to clearing the cache after each page edit.
    """

    return getattr(settings, "WP_CLEAR_CACHE", False)
