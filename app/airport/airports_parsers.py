# coding=utf-8

from app.common.string_methods import get_value_from_regex, get_amount_from_regex, get_int_from_regex
from app.common.target_parse_strings import FUEL_CAPACITY_REGEX, FUEL_STOCK_REGEX, AIRPORT_PLANES_CAPACITY, \
    AIRPORT_NAME_REGEX, AIRPORT_COUNTRY_NAME_REGEX, STOCK_ENGINES_6_REGEX, STOCK_ENGINES_5_REGEX, AIRPORT_CASH_REGEX


def get_country(page):
    country = get_value_from_regex(AIRPORT_COUNTRY_NAME_REGEX, page)
    return country


def get_money(page):
    money_string = get_amount_from_regex(AIRPORT_CASH_REGEX, page)
    return money_string


def get_kerosene_supply(page):
    return get_amount_from_regex(FUEL_STOCK_REGEX, page)


def get_kerosene_capacity(page):
    return get_amount_from_regex(FUEL_CAPACITY_REGEX, page)


def get_engines_supply(page):
    return {
        '5': get_amount_from_regex(STOCK_ENGINES_5_REGEX, page),
        '6': get_amount_from_regex(STOCK_ENGINES_6_REGEX, page)
    }


def get_planes_capacity(page):
    return get_int_from_regex(AIRPORT_PLANES_CAPACITY, page)


def get_airport_name(page):
    return get_value_from_regex(AIRPORT_NAME_REGEX, page).encode('utf-8')
