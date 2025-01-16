from django import template
from django.utils.formats import number_format


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

@register.filter(name='formatted_price')
def formatted_price(value):
    """Formats the price to 2 decimal places with commas and adds the € sign."""
    if value is None:
        return "€0.00"
    return number_format(value, decimal_pos=2, force_grouping=True)
