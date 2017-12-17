from django.views.generic import ListView

from .models import SitePost


class PostListView(ListView):
    model = SitePost
    template_name = 'peregrine/site_post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
