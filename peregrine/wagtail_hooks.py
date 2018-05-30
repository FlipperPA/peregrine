from django.conf import settings
from django.db import connection

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.core import hooks

from .models import Category, PeregrineSettings


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
    This will only keep Wagtail's most recent revisions to a page when it
    is saved, as set in settings. Defaults to None, which saves all
    revisions.
    """

    peregrine_settings = PeregrineSettings.for_site(request.site)

    if peregrine_settings.revisions_to_keep is not None:
        pks_to_delete = page.revisions.order_by('-created_at')[peregrine_settings.revisions_to_keep:].values_list('id', flat=True)
        page.revisions.filter(pk__in=pks_to_delete).delete()

        # If running Zappa with S3 SQLite, perform a vacuum to keep the database size small.
        if settings.DATABASES['default']['ENGINE'] == 'zappa_django_utils.db.backends.s3sqlite':
            cursor = connection.cursor()
            cursor.execute('VACUUM;')
            cursor.close()
