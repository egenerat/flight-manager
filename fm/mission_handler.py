# -*- coding: utf-8 -*-

import datetime
import math
import os
import traceback

from app.airport.airport_builder import build_airport_from_html
from app.airport.airports_methods import switch_to_airport
from app.common.constants import PARSER_AIRPORT_ID
from app.common.exceptions.string_not_found import StringNotFoundException
from app.common.logger import logger
from app.common.http_methods import post_request, get_request
from app.common.string_methods import get_amount, get_value_from_regex
from app.common.target_urls import GENERIC_ACCEPT_MISSION, AIRPORT_PAGE, STAFF_PAGE
from app.missions.mission import get_real_benefit, get_expiry_date, is_mission_feasible
from app.missions.mission_utils import split_missions_list_by_type, is_possible_mission, find_plane_class_for_mission, \
    is_interesting_mission
from app.planes.planes_util2 import split_planes_list_by_type
from fm.databases.database import db_insert_object, db_remove_all_missions
from fm.list_missions import list_missions, list_dest_countries_id_by_mission_type
from fm.models import Mission, Stopover


def enrich_mission_dictionary(mission_dict, expiry_date, country, mission_type):
    stopover_dict = mission_dict.pop('stopover')
    stopover = None
    a_mission = Mission(**mission_dict)
    a_mission.expiry_date = expiry_date.replace(tzinfo=None)
    a_mission.origin_country = country
    a_mission.mission_type = mission_type
    plane_class = find_plane_class_for_mission(a_mission)
    a_mission.revenue_per_hour = get_real_benefit(a_mission, plane_class.price)
    total_hours = a_mission.time_before_departure + \
        math.ceil(a_mission.km_nb / plane_class.speed) * 2
    a_mission.total_time = total_hours
    total_reputation = a_mission.reputation
    if stopover_dict:
        stopover = Stopover(**stopover_dict)
        a_mission.stopover = stopover
        # stopover lasts one hour in the remote airport
        a_mission.total_time += 1
        total_reputation += stopover.reputation
        a_mission.reputation = total_reputation
        a_mission.contract_amount += stopover.revenue
    a_mission.reputation_per_hour = total_reputation / float(total_hours)
    return {
        'a_mission': a_mission,
        'stopover': stopover
    }


def empty_db_missions():
    db_remove_all_missions()


def parse_all_missions():
    switch_to_airport(PARSER_AIRPORT_ID)
    # ANALYSIS
    full_analysis = False
    db_remove_all_missions()
    mission_types = ["4", "5"]
    # ANALYSIS
    # mission_types = ["1", "2", "3"]
    result = list_dest_countries_id_by_mission_type(mission_types)
    # result = {'4':[u'1'], '5':[u'1']}
    expiry_date = get_expiry_date()
    staff_page = get_request(STAFF_PAGE)
    airport_page = get_request(AIRPORT_PAGE)
    current_airport = build_airport_from_html(airport_page, staff_page)
    country = current_airport.country
    for mission_type, countries_list in result.iteritems():
        mission_list = list_missions(mission_type, countries_list)
        for a_mission_dict in mission_list:
            enriched_data = enrich_mission_dictionary(
                a_mission_dict, expiry_date, country, mission_type)
            a_mission = enriched_data['a_mission']
            if (is_possible_mission(a_mission) and is_interesting_mission(a_mission)) or full_analysis:
                a_stopover = enriched_data['stopover']
                if a_stopover:
                    db_insert_object(a_stopover)
                    a_mission.stopover = a_stopover
                db_insert_object(a_mission)


def extract_bonus_from_page(page):
    return get_amount(get_value_from_regex('BONUS de <strong>(.+)</strong>', page))


def are_missions_expired(missions):
    if os.getenv('SKIP_MISSION_REFRESH') == "True":
        return False
    expiry_date = missions[0].expiry_date
    today = datetime.datetime.now()
    return (expiry_date - today) <= datetime.timedelta(0)


def __accept_mission(country_id, plane_id, mission_id, mission_type, stopover):
    bonus = None
    log_message = 'accept mission {} with plane {}'.format(
        mission_id, plane_id)
    post_data = {'id_avion': str(plane_id)}
    if stopover:
        log_message += ' + stopover'
        post_data.update({'active_escale': '1'})
    page = post_request(
        GENERIC_ACCEPT_MISSION.format(
            mission_type=mission_type, mission_id=mission_id, country_id=country_id),
        post_data)
    logger.info(log_message)
    try:
        bonus = extract_bonus_from_page(page)
    except StringNotFoundException:
        error_message = get_value_from_regex('<strong>(.*)</strong>', page)
        logger.error(error_message)
    return bonus


def accept_one_mission(plane_id, a_mission):
    try:
        has_stopover = a_mission.stopover is not None
        __accept_mission(a_mission.country_nb, plane_id, a_mission.mission_nb, a_mission.mission_type,
                         has_stopover)
    except Exception as e:
        exception_text = traceback.format_exc()
        logger.error(exception_text)
        # notify('FM : bug while accepting mission', get_airport().get_airport_name() + '\nThere was a bug while accepting mission :\n' + str(exception_text))


def accept_all_missions_one_type(plane_list, mission_list):
    for a_plane in plane_list:
        found = False
        mission_remaining = []
        for a_mission in mission_list:
            if not found and is_mission_feasible(a_mission, a_plane):
                accept_one_mission(a_plane.plane_id, a_mission)
                found = True
            else:
                mission_remaining.append(a_mission)
        mission_list = mission_remaining


def accept_all_missions(missions_list, plane_list):
    sorted_planes = split_planes_list_by_type(plane_list)
    sorted_missions = split_missions_list_by_type(missions_list)
    if len(sorted_planes['commercial_ready_planes']):
        accept_all_missions_one_type(sorted_planes['commercial_ready_planes'], sorted_missions['missions_for_commercial'])
    if len(sorted_planes['supersonic_ready_planes']):
        accept_all_missions_one_type(sorted_planes['supersonic_ready_planes'], sorted_missions['missions_for_supersonics'])
    if len(sorted_planes['jet_ready_planes']):
        accept_all_missions_one_type(sorted_planes['jet_ready_planes'], sorted_missions['missions_for_jet'])
