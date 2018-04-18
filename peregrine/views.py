from django.conf import settings
from django.contrib.syndication.views import Feed
from django.views.generic import ListView

from wagtail.core.views import serve

from .models import SitePost, PeregrineSettings


class PostsListView(ListView):
    """
    Paginated view of blog posts.
    """
    template_name = 'peregrine/site_post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return SitePost.objects.live().order_by('-post_date')

    def get(self, request, *args, **kwargs):
        peregrine_settings = PeregrineSettings.for_site(request.site)

        if peregrine_settings.landing_page is None or 'name' in kwargs:
            # If a landing page hasn't been set, or 'name' is in kwargs
            # because we're on an author or category page:
            # render list of recent posts
            response = super().get(request, *args, **kwargs)
            return response
        else:
            # There's a landing page set in settings, and no 'name'
            # in kwargs, so we are on the home page:
            # Render the user selected landing page
            return serve(request, peregrine_settings.landing_page.url)

    def get_paginate_by(self, queryset):
        peregrine_settings = PeregrineSettings.for_site(self.request.site)

        return peregrine_settings.post_number


class AuthorPostsListView(PostsListView):
    """
    Paginated view of blog posts by an author.
    """

    def get_queryset(self):
        return SitePost.objects.filter(
            authors__username__iexact=self.kwargs.get('name', None),
        )

    def get_context_data(self, **kwargs):
        context = super(AuthorPostsListView, self).get_context_data(**kwargs)
        context['author'] = self.kwargs.get('name', None)
        return context


class CategoryPostsListView(PostsListView):
    """
    Paginated view of blog posts by category.
    """

    def get_queryset(self):
        return SitePost.objects.filter(
            categories__name__iexact=self.kwargs['name'],
        )

    def get_context_data(self, **kwargs):
        context = super(CategoryPostsListView, self).get_context_data(**kwargs)
        context['category'] = self.kwargs.get('name', None)
        return context


class PostsFeed(Feed):
    """
    RSS feed to blog posts.
    """
    title = settings.WAGTAIL_SITE_NAME
    link = "/rss/"
    description = 'Blog posts from {site_name} as they are published.'.format(
        site_name=settings.WAGTAIL_SITE_NAME,
    )

    def get_object(self, request, *args, **kwargs):
        kwargs['count'] = PeregrineSettings.for_site(request.site).post_number_rss
        return kwargs['count']

    def items(self, count):
        return SitePost.objects.live().order_by('-post_date')[:count]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt

    def item_link(self, item):
        return item.url
