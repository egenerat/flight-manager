# coding=utf-8
import math

from app.common.constants import MAX_KM, KEROSENE_PRICE


# do not add dependency to CommercialPlane here, otherwise cyclic dependency
from app.common.target_parse_strings import SUPERSONICS_MODELS_HTML, COMMERCIAL_MODELS_HTML, JETS_MODELS_HTML


def get_plane_value(new_plane_value, km, kerosene_qty):
    value = (MAX_KM - km) / float(MAX_KM) * new_plane_value
    value += kerosene_qty * KEROSENE_PRICE
    return int(value)


def duration_mission(distance, speed):
    return math.ceil(distance/float(speed))


def calculate_total_consumption_mission(duration, conso_per_hour, passengers_nb, staff_nb):
    # formula is flight_hours * (consumption_per_hour + 3*(passengers_nb+staff))*3/2
    # replacing time by distance/speed
    return duration*(conso_per_hour+3*(passengers_nb+staff_nb))*(3/2.0)


def calculate_real_autonomy_one_way(speed, kerosene_capacity, conso_per_hour, passengers_nb, staff_nb):
    max_duration = 0
    while calculate_total_consumption_mission(max_duration, conso_per_hour, passengers_nb, staff_nb) < kerosene_capacity:
        max_duration+=1
    return (max_duration - 1) * speed

def is_supersonic(string_model):
    return string_model in SUPERSONICS_MODELS_HTML


def is_jet(string_model):
    return string_model in JETS_MODELS_HTML


def is_regular_plane(string_model):
    return string_model in COMMERCIAL_MODELS_HTML
