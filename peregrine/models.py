from django.conf import settings
from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtailcontentstream.models import ContentStreamPage


class Page(ContentStreamPage):
    pass


class Post(ContentStreamPage):
    date = models.DateField("Post Date")
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL)

    content_panels = [
        FieldPanel('authors'),
        FieldPanel('date'),
    ] + ContentStreamPage.content_panels
