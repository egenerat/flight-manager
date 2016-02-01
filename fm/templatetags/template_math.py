from django import template

register = template.Library()

@register.filter
def multiply(x, y):
    return float(x)*float(y)