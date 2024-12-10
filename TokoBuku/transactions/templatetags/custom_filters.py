# your_app/templatetags/custom_filters.py

from django import template

register = template.Library()


@register.filter
def formatted_price(value):
    """Format the price to Indonesian Rupiah."""
    if value is None:
        return "Rp. 0,-"
    return f"Rp. {value:,.0f}".replace(',', '.') + ',-'
