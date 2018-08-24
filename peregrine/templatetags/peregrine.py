from django import template
from django.conf import settings

from ..models import SitePost

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    """
    NB this returns a core.Page, not the implementation-specific model used
    so object-comparison to self will return false as objects would differ
    """
    return context['request'].site.root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


@register.inclusion_tag('peregrine/tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    """
    Retrieves the top menu items - the immediate children of the parent page
    The has_menu_children method is necessary because the bootstrap menu requires
    a dropdown class to be applied to a parent
    """

    # Select any Page type other than SitePosts for menu inclusion.
    menu_items = parent.get_children().filter(
        live=True,
        show_in_menus=True,
    ).exclude(
        content_type__model='sitepost',
    )

    for menu_item in menu_items:
        menu_item.show_dropdown = has_menu_children(menu_item)
    return {
        'calling_page': calling_page,
        'menu_items': menu_items,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('peregrine/tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    """
    Retrieves the children of the top menu items for the drop downs
    """
    menu_items_children = parent.get_children()
    menu_items_children = menu_items_children.live().in_menu()
    return {
        'parent': parent,
        'menu_items_children': menu_items_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('peregrine/tags/top_menu_posts.html', takes_context=True)
def top_menu_posts(context):
    """
    Retrieves the 10 most recent SitePosts for the top menu drop down.
    """
    posts = SitePost.objects.filter(
        live=True,
        show_in_menus=True,
    ).order_by(
        '-post_date',
    )[:10]

    show_posts = posts.count() > 0

    return {
        'posts': posts,
        'show_posts': show_posts,
    }


@register.simple_tag
def settings_value(name):
    """
    Allows a value from Django's settings to be included in a template tag.
    """
    return getattr(settings, name, "")
