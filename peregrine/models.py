from django.conf import settings
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils.timezone import now

from modelcluster.fields import ParentalManyToManyField

# Wagtail 2.0 compatibility - new package paths
try:
    from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
    from wagtail.core.fields import RichTextField
    from wagtail.images.edit_handlers import ImageChooserPanel
    from wagtail.search import index
except ImportError:
    from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
    from wagtail.wagtailcore.fields import RichTextField
    from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
    from wagtail.wagtailsearch import index

from wagtailcontentstream.models import ContentStreamPage


class Settings(models.Model):
    """
    Key / value store for Peregrine's settings.
    """
    key = models.CharField(unique=True, max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        indexes = [
            models.Index(fields=['key'], name='settings_key_idx'),
        ]


class Category(models.Model):
    """
    Categories which a Page or Post item can belong to. A page can belong to
    many categories.
    """
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class SitePage(ContentStreamPage):
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='A featured image that will appear in the site theme header.',
    )
    excerpt = RichTextField(
        features=['bold', 'italic', 'link', 'ol', 'ul'],
        blank=True,
        null=True,
        help_text='An short excerpt or abstract about the content.'
    )
    categories = ParentalManyToManyField(
        'Category',
        blank=True,
        help_text='The categories for the page or post.',
    )
    show_in_menus_default = True

    search_fields = ContentStreamPage.search_fields + [
        index.SearchField('body'),
        index.SearchField('excerpt'),
    ]

    content_panels = [
        FieldPanel('title'),
        ImageChooserPanel('header_image'),
        FieldPanel('excerpt'),
        FieldPanel('categories', widget=CheckboxSelectMultiple),
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = 'Page'


class SitePost(SitePage):
    post_date = models.DateTimeField(
        default=now,
        help_text='The date and time of the post.',
    )
    authors = ParentalManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        help_text='The authors of the post.',
    )
    show_in_menus_default = True

    content_panels = [
        FieldPanel('title'),
        FieldPanel('post_date'),
        FieldPanel('authors'),
        ImageChooserPanel('header_image'),
        FieldPanel('excerpt'),
        FieldPanel('categories', widget=CheckboxSelectMultiple),
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = 'Post'
