from django import template
from django.conf import settings

register = template.Library()


@register.assignment_tag(takes_context=True)
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
    menuitems = parent.get_children().filter(
        live=True,
        show_in_menus=True
    )
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('peregrine/tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    """
    Retrieves the children of the top menu items for the drop downs
    """
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.simple_tag
def settings_value(name):
    """
    Allows a value from Django's settings to be included in a template tag.
    """
    return getattr(settings, name, "")
    print('Hello!')
    print(name)
