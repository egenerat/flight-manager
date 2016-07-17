import re
import traceback

from app.common.logger import logger
from app.common.http_methods import post_request
from app.common.target_urls import GENERIC_ACCEPT_MISSION


def extract_bonus_from_page(page):
    return re.findall('BONUS de <strong>(\d+),(\d+)</strong>', page)


def __accept_mission(country_id, plane_id, mission_id, mission_type):
    page = post_request(GENERIC_ACCEPT_MISSION.format(mission_type = mission_type, mission_id = mission_id, country_id = country_id), {'id_avion': str(plane_id)})
    # Be careful, if re.findall()[0], may introduce list index out of range exception!
    temp_bonus = extract_bonus_from_page(page)
    if len(temp_bonus) == 1:
        bonus = temp_bonus[0][0] + temp_bonus[0][1]
    return bonus


def accept_all_missions(missions_dict, plane_list):
    for country_id in missions_dict:
        for mission_id in missions_dict[country_id]:
            plane_id = plane_list.pop().plane_id
            mission_type = '5' #missions_dict['']
            logger.warning('accept mission : {} with plane {}'.format(mission_id, plane_id))
            try:
                __accept_mission(country_id, plane_id, mission_id, mission_type)
            except Exception as e:
                exception_text = traceback.format_exc()
                logger.error(exception_text)
                # notify('AS : bug while accepting mission', get_airport().get_airport_name() + '\nThere was a bug while accepting mission :\n' + str(exception_text))