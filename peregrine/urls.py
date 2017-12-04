from django.conf.urls import url, include

from wagtail.wagtailcore import urls as wagtail_urls


urlpatterns = [
    url(r'', include(wagtail_urls)),
]
