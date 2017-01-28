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


@register.filter
def mission_type_to_string(mission_type):
    return {
        '1': 'Customers',
        '2': 'Freight',
        '3': 'Quick',
        '4': 'Supersonics',
        '5': 'Jet',
    }.get(mission_type)
