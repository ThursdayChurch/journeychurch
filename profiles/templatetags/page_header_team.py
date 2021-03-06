from django import template

register = template.Library()

# Page Header for Teams:
# Custom Tag that can be accessed by {% page_header_team %}. Embeds page header.
@register.inclusion_tag("profiles/header.html")
def page_header_team(page, teams, current_slug):

    return {'page':page, 'teams': teams, 'current_slug': current_slug}
