from django import template
from django.utils.dates import MONTHS

register = template.Library()


@register.filter(name='monthname')
def monthname(value):
    """Removes all values of arg from the given string"""
    print(MONTHS)
    return MONTHS.get(value, value)
