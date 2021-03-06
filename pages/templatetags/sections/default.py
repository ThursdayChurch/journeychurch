from django import template
from django.shortcuts import get_object_or_404
from pages.models import SectionDefault

register = template.Library()

# Default Section:
# Custom Tag that can be accessed by {% default %}. Creates fields for a default type section
@register.inclusion_tag("pages/sections/default.html")
def default(section):

    context = {
        "title": section.display_title,
        "slug": section.slug,
        "background_image": section.background_image,
        "background_color": section.background_color,
        "content": section.content
    }

    return context
