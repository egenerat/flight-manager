# -*- coding: utf-8 -*-

from app.common.constants import USERNAME
from app.common.string_methods import get_value_from_regex, get_values_from_regex, clean_amount
from app.common.target_parse_strings import SALE_AIRPORTS_BEGIN_HTML, SALE_AIRPORT_ID_REGEX
from app.common.target_parse_strings import SALE_AIRPORTS_END_HTML


def build_airport_from_line(html_line):
    table_data = get_values_from_regex('<td class="Vaero\d">(.+?)<\/td>', html_line)
    airport_id = int(get_value_from_regex(SALE_AIRPORT_ID_REGEX, html_line))
    capacity = int(table_data[2])
    reputation = clean_amount(table_data[3])
    cash = clean_amount(table_data[4])
    price = clean_amount(table_data[6])
    vendor = table_data[0]
    return {
        'airport_id': airport_id,
        'cash': cash,
        'capacity': capacity,
        'reputation': reputation,
        'price': price,
        'vendor': vendor
    }


def build_airports_list(page):
    result = []

    index_begin = page.find(SALE_AIRPORTS_BEGIN_HTML)
    index_end = page.find(SALE_AIRPORTS_END_HTML)

    page = page[index_begin: index_end]
    airports_html_list = page.split("</tr><tr>")[1:]

    for an_airport_html in airports_html_list:
        result.append(build_airport_from_line(an_airport_html))
    return result


def find_new_airports(old_list, new_list):
    old_list_price = []
    result = []
    for i in old_list:
        old_list_price.append(i.price)
    for i in new_list:
        # check if already exists (price)
        if i['price'] not in old_list_price and not i['vendor'] == USERNAME:
            result.append(i)
    return result
