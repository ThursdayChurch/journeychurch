from django import template
from django.shortcuts import get_object_or_404
from pages.models import NavigationMenu

register = template.Library()

# Navigation menu:
# Custom Tag that can be accessed by {{ navigation }}. Sends NavigationMenu items to navigation.html.
@register.inclusion_tag("pages/navigation.html")
def navigation(title='Main', inline=True):

    # get navigation menu
    menu = get_object_or_404(NavigationMenu, title=title)

    # get all of its navigation items
    navigation_items = menu.navigationitem_set.all().order_by('order')

    return {'navigation_items': navigation_items, 'inline': inline}
