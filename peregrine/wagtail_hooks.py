from django.core.cache import cache

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register
)

from wagtail.core import hooks

from .models import Category
from .settings import get_clear_cache


class CategoryAdmin(ModelAdmin):
    model = Category
    menu_label = 'Grid Categories'
    menu_icon = 'fa-folder-open'
    add_to_settings_menu = False
    list_display = ('name',)
    search_fields = ('name',)


class PeregrineAdminGroup(ModelAdminGroup):
    menu_label = 'Peregrine'
    menu_icon = 'fa-th'
    menu_order = 400
    items = (CategoryAdmin,)


modeladmin_register(PeregrineAdminGroup)


@hooks.register('after_edit_page')
def clear_page_cache(request, page):
    """
    This will clear Django's entire cache after a page edit. It is ugly,
    but Django's cache mechanism doesn't currently support a way to easily
    depending on the value of is_staff() and (if present) is_faculty.
    """

    if get_clear_cache():
        cache.clear()
