from django.conf.urls import url, include

from wagtail.core import urls as wagtail_urls

from .views import PostListView

urlpatterns = [
    url(r'^$', PostListView.as_view()),
    url(r'', include(wagtail_urls)),
]
