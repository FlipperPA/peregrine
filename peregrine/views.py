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


class PostsFeed(Feed):
    """
    RSS feed to blog posts.
    """
    title = "My blog articles"
    link = "/blogs-feed/"
    description = "All of my blogs as they are published"

    def items(self):
        return SitePost.objects.live().order_by('-post_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt

    def item_link(self, item):
        return item.full_url
