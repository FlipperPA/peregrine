from django.conf import settings
from django.contrib.syndication.views import Feed
from django.views.generic import ListView

from .models import SitePost


class PostsListView(ListView):
    """
    Paginated view of blog posts.
    """
    model = SitePost
    template_name = 'peregrine/site_post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-post_date']


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

    def items(self):
        return SitePost.objects.live().order_by('-post_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt

    def item_link(self, item):
        return item.url
