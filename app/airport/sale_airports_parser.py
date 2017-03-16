# -*- coding: utf-8 -*-

import re

from app.common.constants import OWN_PSEUDO
from app.common.string_methods import get_amount, get_value_from_regex, get_values_from_regex
from app.common.target_parse_strings import SALE_AIRPORTS_BEGIN_HTML, SALE_ONE_AIRPORT_BEGIN_HTML, \
    SALE_ONE_AIRPORT_END_HTML, SALE_AIRPORT_ID_REGEX, SALE_AIRPORT_REPUTATION_REGEX, SALE_AIRPORT_CASH_REGEX, \
    SALE_AIRPORT_PRICE_REGEX, SALE_AIRPORT_PSEUDO
from app.common.target_parse_strings import SALE_AIRPORTS_END_HTML


def build_airports_list(page):
    result = []

    index_begin = page.find(SALE_AIRPORTS_BEGIN_HTML)
    index_end = page.find(SALE_AIRPORTS_END_HTML)

    page = page[index_begin: index_end]

    begin_one_airport = SALE_ONE_AIRPORT_BEGIN_HTML
    end_one_airport = SALE_ONE_AIRPORT_END_HTML

    indexes_begin_airport = [(m.start()) for m in re.finditer(begin_one_airport, page)][::2]
    indexed_end_airport = [(m.start()) for m in re.finditer(end_one_airport, page)]

    for i in range(0, len(indexes_begin_airport)):
        a_airport_text = page[indexes_begin_airport[i]:indexed_end_airport[i]]
        airport_id = get_value_from_regex(SALE_AIRPORT_ID_REGEX, a_airport_text)
        capacity_reputation = get_values_from_regex(SALE_AIRPORT_REPUTATION_REGEX, a_airport_text)
        cash = get_amount(get_values_from_regex(SALE_AIRPORT_CASH_REGEX, a_airport_text)[1])
        price = get_amount(get_value_from_regex(SALE_AIRPORT_PRICE_REGEX, a_airport_text))
        saler = get_value_from_regex(SALE_AIRPORT_PSEUDO, page)
        if not saler == OWN_PSEUDO:
            an_airport = {
                'airport_id': int(airport_id),
                'cash': cash,
                'capacity': int(capacity_reputation[0]),
                'reputation': get_amount(capacity_reputation[1]),
                'price': price,
            }
            result.append(an_airport)
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
