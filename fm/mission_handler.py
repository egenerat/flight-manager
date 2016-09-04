# coding=utf-8

import re
import traceback

import datetime

import math

import fm.singleton_session
from app.airport.airport_builder import build_airport
from app.common.logger import logger
from app.common.http_methods import post_request, get_request
from app.common.target_urls import GENERIC_ACCEPT_MISSION, AIRPORT_PAGE, STAFF_PAGE
from app.missions.mission import get_real_benefit, get_expiry_date
from app.missions.mission_utils import split_missions_list_by_type, is_possible_mission, find_plane_class_for_mission, \
    is_interesting_mission
from app.planes.planes_util2 import split_planes_list_by_type
from fm.databases.database import db_insert_object, db_remove_all_missions
from fm.list_missions import list_missions, list_countries
from fm.models import Mission


def enrich_mission_dictionary(mission_dict, expiry_date, country, mission_type):
    a_mission = Mission(**mission_dict)
    a_mission.expiry_date = expiry_date.replace(tzinfo=None)
    a_mission.origin_country = country
    a_mission.mission_type = mission_type
    plane_class = find_plane_class_for_mission(a_mission)
    a_mission.revenue_per_hour = get_real_benefit(a_mission, plane_class.price)
    total_hours = a_mission.time_before_departure + math.ceil(a_mission.km_nb / plane_class.speed) * 2
    a_mission.total_time = total_hours
    a_mission.reputation_per_hour = int(a_mission.reputation / total_hours)
    return a_mission


def parse_all_missions():
    db_remove_all_missions()
    result = list_countries()
    expiry_date = get_expiry_date()
    staff_page = get_request(STAFF_PAGE)
    airport_page = get_request(AIRPORT_PAGE)
    current_airport = build_airport(airport_page, staff_page)
    country = current_airport.country
    for mission_type, countries_list in result.iteritems():
        mission_list = list_missions(mission_type, countries_list)
        for a_mission_dict in mission_list:
            a_mission = enrich_mission_dictionary(a_mission_dict, expiry_date, country, mission_type)
            if is_possible_mission(a_mission) and is_interesting_mission(a_mission):
                db_insert_object(a_mission)


def extract_bonus_from_page(page):
    return re.findall('BONUS de <strong>(\d+),(\d+)</strong>', page)


def are_missions_expired(missions):
    # TODO improve environment handling
    # if fm.singleton_session.local_mode:
    #     return False
    expiry_date = missions[0].expiry_date
    today = datetime.datetime.now()
    return (expiry_date - today) <= datetime.timedelta(0)


def __accept_mission(country_id, plane_id, mission_id, mission_type):
    bonus = None
    logger.info('accept mission: {} with plane {}'.format(mission_id, plane_id))
    page = post_request(
        GENERIC_ACCEPT_MISSION.format(mission_type=mission_type, mission_id=mission_id, country_id=country_id),
        {'id_avion': str(plane_id)})
    # Be careful, if re.findall()[0], may introduce list index out of range exception!
    temp_bonus = extract_bonus_from_page(page)
    if len(temp_bonus) == 1:
        bonus = int(temp_bonus[0][0] + temp_bonus[0][1])
    return bonus


def temp(plane_list, a_mission):
    plane_id = plane_list.pop().plane_id
    try:
        bonus = __accept_mission(a_mission.country_nb, plane_id, a_mission.mission_nb, a_mission.mission_type)
    except Exception as e:
        exception_text = traceback.format_exc()
        logger.error(exception_text)
        # notify('FM : bug while accepting mission', get_airport().get_airport_name() + '\nThere was a bug while accepting mission :\n' + str(exception_text))


def accept_all_missions(missions_list, plane_list):
    sorted_planes = split_planes_list_by_type(plane_list)
    sorted_missions = split_missions_list_by_type(missions_list)
    for a_mission in sorted_missions['missions_for_commercial'][:len(sorted_planes['commercial_ready_planes'])]:
        temp(sorted_planes['commercial_ready_planes'], a_mission)
    for a_mission in sorted_missions['missions_for_supersonics'][:len(sorted_planes['supersonic_ready_planes'])]:
        temp(sorted_planes['supersonic_ready_planes'], a_mission)
    for a_mission in sorted_missions['missions_for_jet'][:len(sorted_planes['jet_ready_planes'])]:
        temp(sorted_planes['jet_ready_planes'], a_mission)
