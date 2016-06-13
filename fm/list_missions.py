from app.common.constants import SUPERSONICS_MISSION_PAGE
from app.common.http_methods import post_request
from app.common.target_urls import SUPERSONICS_MISSION_PAGE
from app.missions.missionparser import parse_all_missions_in_page, get_country_list


def list_missions():
    result = []
    supersonics_country = get_country_list()
    for country_id in supersonics_country:
        page = post_request(SUPERSONICS_MISSION_PAGE, {u'id_pays': country_id})
        temp = parse_all_missions_in_page(page, country_id)
        result.append(temp)
    return result




