import re
import traceback

from app.common.logger import logger
from app.common.http_methods import post_request
from app.common.target_urls import GENERIC_ACCEPT_MISSION
from app.missions.mission_utils import split_missions_list_by_type
from app.planes.planes_util2 import split_planes_list_by_type


def extract_bonus_from_page(page):
    return re.findall('BONUS de <strong>(\d+),(\d+)</strong>', page)


def __accept_mission(country_id, plane_id, mission_id, mission_type):
    logger.warning('accept mission : {} with plane {}'.format(mission_id, plane_id))
    page = post_request(GENERIC_ACCEPT_MISSION.format(mission_type = mission_type, mission_id = mission_id, country_id = country_id), {'id_avion': str(plane_id)})
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
        # notify('AS : bug while accepting mission', get_airport().get_airport_name() + '\nThere was a bug while accepting mission :\n' + str(exception_text))


def accept_all_missions(missions_list, plane_list):
    sorted_planes = split_planes_list_by_type(plane_list)
    sorted_missions = split_missions_list_by_type(missions_list)
    for a_mission in sorted_missions['missions_for_commercial'][:len(sorted_planes['commercial_ready_planes'])]:
        temp(sorted_planes['commercial_ready_planes'], a_mission)
    for a_mission in sorted_missions['missions_for_supersonics'][:len(sorted_planes['supersonic_ready_planes'])]:
        temp(sorted_planes['supersonic_ready_planes'], a_mission)
    for a_mission in sorted_missions['missions_for_jet'][:len(sorted_planes['jet_ready_planes'])]:
        temp(sorted_planes['jet_ready_planes'], a_mission)