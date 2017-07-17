# -*- coding: utf-8 -*-

from app.common.constants import OWN_PSEUDO
from app.common.string_methods import get_amount, get_value_from_regex, get_values_from_regex
from app.common.target_parse_strings import SALE_AIRPORTS_BEGIN_HTML, \
    SALE_AIRPORT_ID_REGEX, SALE_AIRPORT_REPUTATION_REGEX, SALE_AIRPORT_CASH_REGEX, \
    SALE_AIRPORT_PRICE_REGEX, SALE_AIRPORT_PSEUDO
from app.common.target_parse_strings import SALE_AIRPORTS_END_HTML


def build_airport_from_line(html_line):
    airport_id = get_value_from_regex(SALE_AIRPORT_ID_REGEX, html_line)
    capacity_reputation = get_values_from_regex(SALE_AIRPORT_REPUTATION_REGEX, html_line)
    cash = get_amount(get_values_from_regex(SALE_AIRPORT_CASH_REGEX, html_line)[1])
    price = get_amount(get_value_from_regex(SALE_AIRPORT_PRICE_REGEX, html_line))
    vendor = get_value_from_regex(SALE_AIRPORT_PSEUDO, html_line)
    if not vendor == OWN_PSEUDO:
        an_airport = {
            'airport_id': int(airport_id),
            'cash': cash,
            'capacity': int(capacity_reputation[0]),
            'reputation': get_amount(capacity_reputation[1]),
            'price': price,
            'vendor': vendor
        }
    return an_airport


def build_airports_list(page):
    result = []

    index_begin = page.find(SALE_AIRPORTS_BEGIN_HTML)
    index_end = page.find(SALE_AIRPORTS_END_HTML)

    page = page[index_begin: index_end]
    airports_html_list = page.split("</tr><tr>")[1:]

    for an_airport_html in airports_html_list:
        result.append(build_airport_from_line(an_airport_html))
    return result


def __is_element_in_list(a_list, element):
    # TODO dirty
    result = True
    try:
        a_list.index(element)
    except:
        result = False
    return result


def find_new_airports(old_list, new_list):
    old_list_price = []
    result = []
    for i in old_list:
        old_list_price.append(i.price)
    for i in new_list:
        # check if already exists (price)
        if not __is_element_in_list(old_list_price, i['price']):
            result.append(i)
    return result
