# coding=utf-8

import datetime
import math
import re

from app.common.constants import TIME_DIFFERENCE
from app.common.string_methods import get_value_from_regex, everything_between, \
    date_from_regex_result, get_int_from_regex, string_contains, get_amount
from app.common.target_parse_strings import MISSION_AMOUNT_REGEX, MISSION_DEPARTURE_DATE_REGEX, MISSION_TOO_SHORT_HTML, \
    MISSION_DISTANCE_REGEX, MISSIONS_FLIGHT_ATTENDANTS_NB_REGEX, MISSION_REPUTATION_REGEX, MISSIONS_PILOTS_NB_REGEX, \
    MISSION_ID_REGEX, MISSION_PASSENGERS_CARGO_NB_REGEX, MISSIONS_BEGIN_TABLE_HTML, MISSIONS_END_TABLE_HTML, \
    MISSIONS_LINE_SPLIT_HTML, MISSIONS_ONGOING_ID_REGEX, HTML_SELECT_ID_REGEX, STOPOVER_STRING, \
    STOPOVER_TRAVELLERS_NB_REGEX, STOPOVER_REPUTATION_REGEX, STOPOVER_REVENUE_REGEX


def get_country_list(html_page):
    countries_list = re.findall(HTML_SELECT_ID_REGEX, html_page)
    # supersonics_country = ["3", "4", "5", "184", "23", "28", "30", "35", "57", "66", "74", "81", "106", "109", "123",
    # "158", "170", "177", "185", "224", "229"]
    return countries_list


def compute_time_before_departure(departure_date):
    """ datetime.datetime parameter """
    now = datetime.datetime.now()
    diff = departure_date - now
    return diff.days * 24 + int(math.ceil(diff.seconds / 3600.0)) + TIME_DIFFERENCE


def parse_duration_before_departure(html_mission):
    a = get_value_from_regex(MISSION_DEPARTURE_DATE_REGEX, html_mission)
    departure_date = date_from_regex_result(a)
    return compute_time_before_departure(departure_date)


def parse_stopover(stopover_html):
    return {
        'reputation': get_int_from_regex(STOPOVER_REPUTATION_REGEX, stopover_html),
        'travellers_nb': get_int_from_regex(STOPOVER_TRAVELLERS_NB_REGEX, stopover_html),
        'revenue': get_amount(get_value_from_regex(STOPOVER_REVENUE_REGEX, stopover_html))
    }


def parse_one_mission(mission_html, country_nb):
    if not string_contains(MISSION_TOO_SHORT_HTML,
                           mission_html):  # and not string_contains(u"vous n'avez pas d'avion correspondant &agrave; cette mission", mission_html):
        contract_amount = int(''.join(get_value_from_regex(MISSION_AMOUNT_REGEX, mission_html).split(',')))
        time_before_departure = parse_duration_before_departure(mission_html)
        mission_nb = get_int_from_regex(MISSION_ID_REGEX, mission_html)
        a_mission = {
            'country_nb': int(country_nb),
            'mission_nb': mission_nb,
            'travellers_nb': get_int_from_regex(MISSION_PASSENGERS_CARGO_NB_REGEX, mission_html),
            'contract_amount': contract_amount,
            'reputation': get_int_from_regex(MISSION_REPUTATION_REGEX, mission_html),
            'pilots_nb': get_int_from_regex(MISSIONS_PILOTS_NB_REGEX, mission_html),
            'flight_attendants_nb': get_int_from_regex(MISSIONS_FLIGHT_ATTENDANTS_NB_REGEX, mission_html),
            'time_before_departure': time_before_departure,
            'km_nb': get_int_from_regex(MISSION_DISTANCE_REGEX, mission_html),
            'stopover': STOPOVER_STRING in mission_html
        }
        return a_mission


def parse_all_missions_in_page(html_page, country_nb):
    all_missions_one_country = []
    table = everything_between(html_page, MISSIONS_BEGIN_TABLE_HTML, MISSIONS_END_TABLE_HTML)
    missions_html = table.split(MISSIONS_LINE_SPLIT_HTML)[1:]
    for a_mission in missions_html:
        a_mission = parse_one_mission(a_mission, country_nb)
        if a_mission:
            all_missions_one_country.append(a_mission)
    return all_missions_one_country


def get_ongoing_missions(html_page):
    str_list = re.findall(MISSIONS_ONGOING_ID_REGEX, html_page)
    return [int(item) for item in str_list]


def subtract(missions_list, ongoing_missions_id):
    result = []
    for i in missions_list:
        if i.mission_nb not in ongoing_missions_id:
            result.append(i)
    return result
