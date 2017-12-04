from django.conf import settings
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils.timezone import now

from modelcluster.fields import ParentalManyToManyField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtailcontentstream.models import ContentStreamPage


class Category(models.Model):
    """
    Categories which a Page or Post item can belong to. A page can belong to
    many categories.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


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
    categories = ParentalManyToManyField('Category', blank=True)
    show_in_menus_default = True

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
    authors = models.ManyToManyField(
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
