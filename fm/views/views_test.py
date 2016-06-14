import math

from app.airport.Airport import Airport
from app.common.constants import CONCORDE_SPEED
from app.missions.mission import get_expiry_date, get_real_benefit
from django.http import HttpResponse
from fm.databases.database import db_insert_object
from fm.list_missions import list_countries, list_missions
from fm.models import Mission


def test(request):
    page = ''
    result = list_countries()
    for mission_type, countries_list in result.iteritems():
        mission_list = list_missions(mission_type, countries_list)
        current_airport = Airport()
        country = current_airport.get_country()
        expiry_date = get_expiry_date()
        for a_mission_dict in mission_list:
            a_mission = Mission(**a_mission_dict)
            a_mission.expiry_date = expiry_date.replace(tzinfo=None)
            a_mission.revenue_per_hour = get_real_benefit(a_mission)
            a_mission.origin_country = country
            speed = {
                '1': 971,
                '2': 971,
                '3': 971,
                '4': CONCORDE_SPEED,
                '5': 922,
            }[mission_type]
            total_hours = int(a_mission.time_before_departure + math.ceil(a_mission.km_nb / speed) * 2)
            a_mission.total_time = total_hours
            a_mission.reputation_per_hour = int(int(a_mission.reputation) / total_hours)
            a_mission.mission_type = mission_type
            db_insert_object(a_mission)
    return HttpResponse(mission_list)
