from django.urls import include, path, re_path

from wagtail.core import urls as wagtail_urls

from .views import PostsListView, AuthorPostsListView, CategoryPostsListView, PostsFeed

urlpatterns = [
    path('rss/', PostsFeed(), name='peregrine-rss'),
    path('author/<str:name>/', AuthorPostsListView.as_view(), name='posts-author'),
    path('category/<str:name>/', CategoryPostsListView.as_view(), name='posts-category'),
    path('', PostsListView.as_view(), name='posts'),
    re_path(r'', include(wagtail_urls)),
]
