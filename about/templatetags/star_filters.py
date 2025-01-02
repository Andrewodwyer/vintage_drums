from django import template

register = template.Library()


@register.filter
def render_stars(rating):
    """Render stars based on the rating."""
    filled_stars = '★' * rating
    empty_stars = '☆' * (5 - rating)
    return filled_stars + empty_stars
