# -*- coding: utf-8 -*-
import math

from app.common.constants import MAX_KM, KEROSENE_PRICE

# do not add dependency to CommercialPlane here, otherwise cyclic dependency
from app.common.target_strings import SUPERSONICS_MODELS_HTML, COMMERCIAL_MODELS_HTML, JETS_MODELS_HTML

COEFFICIENT = 0.965


# COEFFICIENT = 1

# concorde: around 0.965
# then we take 0.94

def get_plane_value(new_plane_value, km, kerosene_qty):
    value = (MAX_KM - km) / float(MAX_KM) * new_plane_value
    value += kerosene_qty * KEROSENE_PRICE
    return int(value)


def duration_mission_one_way(distance, speed):
    return math.ceil(distance / float(speed))


def calculate_total_consumption_one_way(duration, conso_per_hour, passengers_nb, staff_nb):
    # TODO improve calculation
    # formula is flight_hours * (consumption_per_hour + 3*(passengers_nb+staff))*3/2
    # replacing time by distance/speed
    return duration * (conso_per_hour + 3 * (passengers_nb + staff_nb))


def calculate_real_autonomy_one_way(speed, kerosene_capacity, conso_per_hour, passengers_nb, staff_nb):
    max_duration = 0
    while calculate_total_consumption_one_way(max_duration, conso_per_hour, passengers_nb,
                                              staff_nb) * 3 / 2.0 < COEFFICIENT * kerosene_capacity:
        max_duration += 1
    return (max_duration - 1) * speed


def calculate_autonomy_with_stopover(speed, kerosene_capacity, conso_per_hour, passengers_nb, staff_nb):
    max_duration = 0
    while calculate_total_consumption_one_way(max_duration, conso_per_hour, passengers_nb,
                                              staff_nb) < COEFFICIENT * kerosene_capacity:
        max_duration += 1
    return (max_duration - 1) * speed


def is_supersonic(string_model):
    return string_model in SUPERSONICS_MODELS_HTML


def is_jet(string_model):
    return string_model in JETS_MODELS_HTML


def is_regular_plane(string_model):
    return string_model in COMMERCIAL_MODELS_HTML


if __name__ == '__main__':
    commercial_planes = [
        {
            "capacity": 73000,
            "price": 1100000,
            "speed": 870,
            "consumption": 7000,
            "plane_model": "A300-600"
        },
        {
            "capacity": 68150,
            "price": 1500000,
            "speed": 780,
            "consumption": 8900,
            "plane_model": "A300-600ST"
        },
        {
            "capacity": 61070,
            "price": 625000,
            "speed": 850,
            "consumption": 5800,
            "plane_model": "A310-200"
        },
        {
            "capacity": 29660,
            "price": 425000,
            "speed": 827,
            "consumption": 2000,
            "plane_model": "A319"
        },
        {
            "capacity": 29660,
            "price": 500000,
            "speed": 827,
            "consumption": 2700,
            "plane_model": "A320"
        },
        {
            "capacity": 25920,
            "price": 520000,
            "speed": 827,
            "consumption": 2900,
            "plane_model": "A321"
        },
        {
            "capacity": 97530,
            "price": 850000,
            "speed": 900,
            "consumption": 7200,
            "plane_model": "A330-200"
        },
        {
            "capacity": 97170,
            "price": 1200000,
            "speed": 880,
            "consumption": 7806,
            "plane_model": "A330-300"
        },
        {
            "capacity": 155400,
            "price": 950000,
            "speed": 900,
            "consumption": 7800,
            "plane_model": "A340-200"
        },
        {
            "capacity": 222000,
            "price": 1400000,
            "speed": 918,
            "consumption": 10075,
            "plane_model": "A340-500"
        },
        {
            "capacity": 204500,
            "price": 1450000,
            "speed": 918,
            "consumption": 11378,
            "plane_model": "A340-600"
        },
        {
            "capacity": 150000,
            "price": 925000,
            "speed": 1040,
            "consumption": 10000,
            "plane_model": "A350-900"
        },
        {
            "capacity": 325000,
            "price": 3700000,
            "speed": 1040,
            "consumption": 17000,
            "plane_model": "A380"
        },
        {
            "capacity": 325000,
            "price": 3700000,
            "speed": 1040,
            "consumption": 17000,
            "plane_model": "A380"
        },
        {
            "capacity": 325000,
            "price": 3700000,
            "speed": 1134,
            "consumption": 15470,
            "plane_model": "A380_IV"
        },
        {
            "capacity": 13890,
            "price": 350000,
            "speed": 825,
            "consumption": 2300,
            "plane_model": "B717-200"
        },
        {
            "capacity": 31000,
            "price": 380000,
            "speed": 915,
            "consumption": 7060,
            "plane_model": "B727"
        },
        {
            "capacity": 23828,
            "price": 400000,
            "speed": 908,
            "consumption": 2850,
            "plane_model": "B737-300"
        },
        {
            "capacity": 26020,
            "price": 420000,
            "speed": 850,
            "consumption": 1850,
            "plane_model": "B737-700"
        },
        {
            "capacity": 183380,
            "price": 1750000,
            "speed": 895,
            "consumption": 12000,
            "plane_model": "B747-100"
        },
        {
            "capacity": 241140,
            "price": 1500000,
            "speed": 913,
            "consumption": 11290,
            "plane_model": "B747-400ER"
        },
        {
            "capacity": 216840,
            "price": 2250000,
            "speed": 860,
            "consumption": 12500,
            "plane_model": "B747-400LCF"
        },
        {
            "capacity": 43400,
            "price": 750000,
            "speed": 848,
            "consumption": 4900,
            "plane_model": "B757-300"
        },
        {
            "capacity": 90916,
            "price": 925000,
            "speed": 854,
            "consumption": 6300,
            "plane_model": "B767-200ER"
        },
        {
            "capacity": 171170,
            "price": 1350000,
            "speed": 890,
            "consumption": 7700,
            "plane_model": "B777-200ER"
        },
        {
            "capacity": 171170,
            "price": 1350000,
            "speed": 970,
            "consumption": 7007,
            "plane_model": "B777-200ER_IV"
        },
        {
            "capacity": 202290,
            "price": 1000000,
            "speed": 905,
            "consumption": 10280,
            "plane_model": "B777-200LR"
        },
        {
            "capacity": 126903,
            "price": 1050000,
            "speed": 902,
            "consumption": 7300,
            "plane_model": "B787"
        },
        {
            "capacity": 146155,
            "price": 1150000,
            "speed": 945,
            "consumption": 10900,
            "plane_model": "MD-11"
        },
        {
            "capacity": 171170,
            "price": 1350000,
            "speed": 890,
            "consumption": 7700,
            "plane_model": "B777-200ER"
        }]
    supersonics_plane = [{
        "capacity": 119500,
        "price": 12590000,
        "speed": 2250,
        "consumption": 25625,
        "plane_model": "Concorde"
    },
        {
            "capacity": 112300,
            "price": 14285000,
            "speed": 2430,
            "consumption": 26180,
            "plane_model": "Tu-144"
        }
    ]
    jet_planes = [{
        "capacity": 6775,
        "price": 1600000,
        "speed": 850,
        "consumption": 850,
        "plane_model": "Challenger 300"
    },
        {
            "capacity": 9500,
            "price": 1980000,
            "speed": 850,
            "consumption": 1078,
            "plane_model": "Challenger 605"
        },
        {
            "capacity": 10650,
            "price": 1750000,
            "speed": 818,
            "consumption": 1620,
            "plane_model": "Challenger 850 ER"
        },
        {
            "capacity": 20325,
            "price": 2350000,
            "speed": 904,
            "consumption": 2067,
            "plane_model": "Global 5000"
        },
        {
            "capacity": 25382,
            "price": 2650000,
            "speed": 905,
            "consumption": 2014,
            "plane_model": "Global Express XRS"
        },
        {
            "capacity": 3811,
            "price": 1550000,
            "speed": 863,
            "consumption": 750,
            "plane_model": "Learjet 60XR"
        },
        {
            "capacity": 2650,
            "price": 1430000,
            "speed": 773,
            "consumption": 590,
            "plane_model": "Cessna Citation CJ3"
        },
        {
            "capacity": 7270,
            "price": 1700000,
            "speed": 848,
            "consumption": 1140,
            "plane_model": "Cessna Citation Sovereign"
        },
        {
            "capacity": 7300,
            "price": 1850000,
            "speed": 934,
            "consumption": 1130,
            "plane_model": "Cessna Citation X"
        },
        {
            "capacity": 4400,
            "price": 1500000,
            "speed": 815,
            "consumption": 1040,
            "plane_model": "Cessna Citation XLS"
        },
        {
            "capacity": 5203,
            "price": 1300000,
            "speed": 750,
            "consumption": 1084,
            "plane_model": "Falcon 20"
        },
        {
            "capacity": 9400,
            "price": 1850000,
            "speed": 850,
            "consumption": 1135,
            "plane_model": "Falcon 2000 EX"
        },
        {
            "capacity": 8767,
            "price": 1780000,
            "speed": 797,
            "consumption": 1155,
            "plane_model": "Falcon 50 EX"
        },
        {
            "capacity": 18050,
            "price": 2390000,
            "speed": 922,
            "consumption": 1510,
            "plane_model": "Falcon 7X"
        },
        {
            "capacity": 11825,
            "price": 2050000,
            "speed": 797,
            "consumption": 1130,
            "plane_model": "Falcon 900 EX"
        },
        {
            "capacity": 6000,
            "price": 1650000,
            "speed": 850,
            "consumption": 933,
            "plane_model": "Gulfstream 150"
        },
        {
            "capacity": 8750,
            "price": 1830000,
            "speed": 850,
            "consumption": 1180,
            "plane_model": "Gulfstream 200"
        },
        {
            "capacity": 17150,
            "price": 2100000,
            "speed": 850,
            "consumption": 1808,
            "plane_model": "Gulfstream 450"
        },
        {
            "capacity": 20500,
            "price": 2250000,
            "speed": 904,
            "consumption": 1725,
            "plane_model": "Gulfstream 500"
        },
        {
            "capacity": 24000,
            "price": 2800000,
            "speed": 904,
            "consumption": 1735,
            "plane_model": "Gulfstream 550"
        }]

    passengers_nb = 50
    staff_nb = 4
    plane_list = commercial_planes
    for plane in plane_list:
        plane['autonomy_one_way'] = calculate_real_autonomy_one_way(plane['speed'], plane['capacity'],
                                                                    plane['consumption'], passengers_nb, staff_nb)
        plane['autonomy_stopover'] = calculate_autonomy_with_stopover(plane['speed'], plane['capacity'],
                                                                      plane['consumption'], passengers_nb, staff_nb)

    criteria = 'autonomy_one_way'
    # criteria = 'autonomy_stopover'
    ordered = sorted(plane_list, key=lambda k: k[criteria])
    for i in ordered:
        print("{}: {}".format(i['plane_model'], i[criteria]))
