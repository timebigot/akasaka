from django import template
import re

register = template.Library()

@register.filter
def imager(value):
    name = value.lower()
    name = re.sub(r' ', '_', name)
    return name
