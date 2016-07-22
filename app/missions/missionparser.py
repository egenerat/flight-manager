# coding=utf-8

import datetime
import math
import re

from app.common.constants import TIME_DIFFERENCE
from app.common.string_methods import get_value_from_regex, everything_between, \
    date_from_regex_result, get_int_from_regex, string_contains


def get_country_list(html_page):
    countries_list = re.findall(u'<option value="(\d{1,3})"', html_page)
    # supersonics_country = ["3", "4", "5", "184", "23", "28", "30", "35", "57", "66", "74", "81", "106", "109", "123",
    # "158", "170", "177", "185", "224", "229"]
    return countries_list


def compute_time_before_departure(departure_date):
    """ datetime.datetime parameter """
    now = datetime.datetime.now()
    diff = departure_date - now
    return diff.days * 24 + int(math.ceil(diff.seconds / 3600.0)) + TIME_DIFFERENCE


def parse_duration_before_departure(html_mission):
    a = get_value_from_regex(
        u'<td class="Mpossibles2">Date d&eacute;part : (\d+)/(\d+)/(\d+) à (\d+):(\d+)</td>', html_mission)
    departure_date = date_from_regex_result(a)
    return compute_time_before_departure(departure_date)


def parse_one_mission(mission_html, country_nb):
    if not string_contains(u'Mission impossible : la distance entre cette ville et votre aéroport est trop courte',
                           mission_html):  # and not string_contains(u"vous n'avez pas d'avion correspondant &agrave; cette mission", mission_html):
        temp2 = get_value_from_regex(u'Contrat : <font color="red">(\d+,\d+) \$</font>', mission_html)
        contract_amount = int(''.join(temp2.split(',')))
        time_before_departure = parse_duration_before_departure(mission_html)
        a_mission = {
            u'country_nb': int(country_nb),
            u'mission_nb': get_int_from_regex(u'Mission (\d+)</strong>', mission_html),
            u'travellers_nb': get_int_from_regex(u'Nombre de (?:passagers|marchandises) : <strong>(\d+)</strong>',
                                                 mission_html),
            u'contract_amount': contract_amount,
            u'reputation': get_int_from_regex(
                u'<td class="Mpossibles2">R&eacute;putation &agrave; gagner : (\d+)</td>', mission_html),
            u'pilots_nb': get_int_from_regex(u'équipage requis : <strong>(\d+)</strong> pilote', mission_html),
            u'flight_attendants_nb': get_int_from_regex(u'<strong>(\d+)</strong> hôtesse', mission_html),
            u'time_before_departure': time_before_departure,
            u'km_nb': get_int_from_regex(u'<td class="Mpossibles2">Distance : <strong>(\d+)</strong> km</td>',
                                         mission_html)
        }
        return a_mission


def parse_all_missions_in_page(html_page, country_nb):
    all_missions_one_country = []
    table = everything_between(html_page, u'Aller en bas de page', u'Aller en haut de page')
    missions_html = table.split(u'<table class="Mpossibles">')[1:]
    for a_mission in missions_html:
        a_mission = parse_one_mission(a_mission, country_nb)
        if a_mission:
            all_missions_one_country.append(a_mission)
    return all_missions_one_country


def get_ongoing_missions(html_page):
    str_list = re.findall('<td class="Taffichage3">Mission (\d+)</td>', html_page)
    return [int(item) for item in str_list]


def subtract(missions_list, ongoing_missions_id):
    result = []
    for i in missions_list:
        if not i.mission_nb in ongoing_missions_id:
            result.append(i)
    return result
