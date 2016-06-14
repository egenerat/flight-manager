from app.common.http_methods import post_request, get_request
from app.common.target_urls import GENERIC_MISSION_PAGE
from app.missions.missionparser import parse_all_missions_in_page, get_country_list


def list_missions(mission_type, countries_list):
    result = []
    countries_list = [countries_list[0]]
    for country_id in countries_list:
        page = post_request(GENERIC_MISSION_PAGE + mission_type, {u'id_pays': country_id})
        temp = parse_all_missions_in_page(page, country_id)
        result.append(temp)
    return result


def list_countries():
    result = {}
    mission_types = [ "1" , "2", "3", "4", "5"]
    for i in mission_types:
        html_page = get_request(GENERIC_MISSION_PAGE + i)
        result[i] = get_country_list(html_page)
    return result




