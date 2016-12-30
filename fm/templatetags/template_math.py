from app.common.countries import countries
from django import template

register = template.Library()


@register.filter
def multiply(x, y):
    return float(x) * float(y)


@register.filter
def country_id_to_name(country_id):
    country_id = str(country_id)
    return countries[country_id]


