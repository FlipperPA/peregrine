from django.conf import settings
from django.db import models
from django.utils.timezone import now

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtailcontentstream.models import ContentStreamPage


class Page(ContentStreamPage):
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    excerpt = RichTextField(
        features=['bold', 'italic', 'link', 'ol', 'ul'],
        blank=True,
        null=True,
    )

    content_panels = [
        ImageChooserPanel('header_image'),
        FieldPanel('excerpt'),
    ] + ContentStreamPage.content_panels


class Post(Page):
    post_date = models.DateTimeField(
        default=now,
    )
    authors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
    )

    content_panels = [
        FieldPanel('post_date'),
        FieldPanel('authors'),
    ] + Page.content_panels
