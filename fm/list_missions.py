# coding=utf-8

from app.common.http_methods import post_request, get_request
from app.common.target_urls import GENERIC_MISSION_PAGE
from app.missions.missionparser import parse_all_missions_in_page, get_country_list


def list_missions(mission_type, countries_list):
    result = []
    countries_list = countries_list
    for country_id in countries_list:
        page = post_request(GENERIC_MISSION_PAGE.format(mission_type=mission_type), {u'id_pays': country_id})
        countries_missions = parse_all_missions_in_page(page, country_id)
        result += countries_missions
    return result


def list_dest_countries_id_by_mission_type():
    """ returns the list of countries available for each mission_type """
    result = {}
    mission_types = ["4", "5"]
    #ANALYSIS
    # mission_types = ["1", "2", "3", "4", "5"]
    for i in mission_types:
        html_page = get_request(GENERIC_MISSION_PAGE.format(mission_type=i))
        result[i] = get_country_list(html_page)

    # import itertools
    # print("{} requests to be sent".format(len(list(itertools.chain.from_iterable(result.values())))))
    return result




