# coding=utf-8

import datetime
import math

from app.common.constants import CONCORDE_SPEED, CONCORDE_PRICE

MONDAY_DAY_OF_WEEK = 0


def get_expiry_date():
    today = datetime.datetime.now()
    time_before_next_monday = (MONDAY_DAY_OF_WEEK - today.weekday()) % 7
    if time_before_next_monday == 0:
        time_before_next_monday = 7
    return today + datetime.timedelta(time_before_next_monday)


def subtract(missions_list, ongoing_missions_id):
    result = []
    for i in missions_list:
        if not i.mission_nb in ongoing_missions_id:
            result.append(i)
    return result


def get_real_benefit(a_mission):
    # TODO: to make it accurate:
    # - add the cost of maintenance
    # - add the time of change engines
    # add the part of the engines that may not be used
    # add the cost of staff
    # TODO not only works for concorde!!!
    revenue = a_mission.contract_amount
    total_hours = a_mission.time_before_departure + math.ceil(a_mission.km_nb / CONCORDE_SPEED) * 2
    plane_use = ((a_mission.km_nb * 2) / 500000.0) * CONCORDE_PRICE
    revenue -= plane_use
    revenue_per_hour = revenue / total_hours
    return int(revenue_per_hour)


def kerosene_consumed(mission, plane):
    # Un surplus de 3 litres par heure par passager(ou colis) et membre d'équipage. A noter que l'avion consomme 2 fois moins sur le trajet retour.'
    # Il faut également tenir compte d'une surconsommation liée aux phases de décollage et d' atterrissage.
    # TODO
    return 0


def hours_consumed(mission_km, plane_speed):
    hours_float = mission_km / float(plane_speed)
    return int(math.ceil(hours_float))


def is_mission_feasible(mission, plane):
    return False
