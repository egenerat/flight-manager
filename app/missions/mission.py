# -*- coding: utf-8 -*-

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
    revenue = a_mission.contract_amount
    total_hours = a_mission.time_before_departure + math.ceil(a_mission.km_nb / CONCORDE_SPEED) * 2
    plane_use = ((a_mission.km_nb * 2) / 500000.0) * CONCORDE_PRICE
    revenue -= plane_use
    revenue_per_hour = revenue / total_hours
    return int(revenue_per_hour)


def kerozene_consumed():
    return 0


def hours_consumed(mission_km, plane_speed):
    return 0