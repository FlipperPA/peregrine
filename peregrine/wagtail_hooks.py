from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register
)

from .models import Category


class CategoryAdmin(ModelAdmin):
    model = Category
    menu_label = 'Peregrine Categories'
    menu_icon = 'list-ul'
    add_to_settings_menu = True
    list_display = ('name',)
    search_fields = ('name',)


modeladmin_register(CategoryAdmin)


@hooks.register('after_edit_page')
def delete_old_revisions(request, page):
    """
    This will clear Django's entire cache after a page edit. It is ugly,
    but Django's cache mechanism doesn't currently support a way to easily
    depending on the value of is_staff() and (if present) is_faculty.
    """

    revisions_to_keep = revisions_to_keep()
    if revisions_to_keep is not None:
        pks_to_delete = page.revisions.order_by('-created_at')[revisions_to_keep:].values_list('id', flat=True)
        page.revisions.filter(pk__in=pks_to_delete).delete()
