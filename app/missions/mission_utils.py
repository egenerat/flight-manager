# coding=utf-8
from app.common.constants import MISSION_REPUTATION_MINIMUM_INTERESTING
from app.common.constants_strategy import JET_MODEL_TO_BE_USED, COMMERCIAL_MODEL_TO_BE_USED, SUPERSONIC_MODEL_TO_BE_USED


def split_missions_list_by_type(missions_list):
    commercial_missions = []
    supersonics_missions = []
    jets_missions = []
    for i in missions_list:
        list_to_append = {
            '1': commercial_missions,
            '3': commercial_missions,
            '2': commercial_missions,
            '4': supersonics_missions,
            '5': jets_missions,
        }[i.mission_type]
        list_to_append.append(i)
    return {
        'missions_for_commercial': commercial_missions,
        'missions_for_supersonics': supersonics_missions,
        'missions_for_jet': jets_missions
    }


def find_plane_class_for_mission(mission):
    return {
        '1': COMMERCIAL_MODEL_TO_BE_USED,
        '2': COMMERCIAL_MODEL_TO_BE_USED,
        '3': COMMERCIAL_MODEL_TO_BE_USED,
        '4': SUPERSONIC_MODEL_TO_BE_USED,
        '5': JET_MODEL_TO_BE_USED
    }[mission.mission_type]


def is_possible_mission(mission):
    plane_class = find_plane_class_for_mission(mission)
    if mission.km_nb <= plane_class.speed:
        return False
    if mission.stopover:
        result = mission.km_nb < plane_class.plane_range_stopover
    else:
        result = mission.km_nb < plane_class.plane_range
    return result and mission.travellers_nb < plane_class.plane_capacity


def is_interesting_mission(mission):
    # if mission.revenue_per_hour < 0, plane usage > revenues
    return mission.reputation_per_hour > MISSION_REPUTATION_MINIMUM_INTERESTING  # and mission.revenue_per_hour > 0


def sort_missions_by_type(mission_list):
    customers_missions = []
    fret_missions = []
    quick_missions = []
    supersonic_missions = []
    jet_missions = []
    for a_mission in mission_list:
        typed_list = {
            '1': customers_missions,
            '2': fret_missions,
            '3': quick_missions,
            '4': supersonic_missions,
            '5': jet_missions,
        }[a_mission.mission_type]
        typed_list.append(a_mission)
    return {
        '1': customers_missions,
        '2': fret_missions,
        '3': quick_missions,
        '4': supersonic_missions,
        '5': jet_missions,
    }


def planes_needed_by_category(mission_list):
    sorted_missions = sort_missions_by_type(mission_list)
    return {
        'Commercial': len(sorted_missions['1']) + len(sorted_missions['2']) + len(sorted_missions['3']),
        'Supersonics': len(sorted_missions['4']),
        'Jets': len(sorted_missions['5']),
    }
