from django.conf.urls import url, include

from wagtail.core import urls as wagtail_urls

from .views import PostsListView, PostsFeed

urlpatterns = [
    url(r'rss/$', PostsFeed(), name='peregrine-rss'),
    url(r'^$', PostsListView.as_view()),
    url(r'', include(wagtail_urls)),
]
