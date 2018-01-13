from django.urls import include, path, re_path

from wagtail.core import urls as wagtail_urls

from .views import PostsListView, PostsFeed

urlpatterns = [
    path('rss/', PostsFeed(), name='peregrine-rss'),
    path('', PostsListView.as_view(), name='posts'),
    re_path(r'', include(wagtail_urls)),
]
