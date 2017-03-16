# -*- coding: utf-8 -*-

from app.common.string_methods import get_numeric_values_regex, get_int_from_regex
from app.common.target_parse_strings import FLIGHT_ATTENDANTS_REGEX, PILOTS_REGEX, MECHANICS_REGEX


def get_pilots(page):
    total_pilots, busy_pilots = get_numeric_values_regex(PILOTS_REGEX, page)
    return total_pilots, busy_pilots


def get_flight_attendants(page):
    total_flight_attendants, busy_flight_attendants = get_numeric_values_regex(FLIGHT_ATTENDANTS_REGEX, page)
    return total_flight_attendants, busy_flight_attendants


def get_mechanics(page):
    return get_int_from_regex(MECHANICS_REGEX, page)
