# coding=utf-8

from app.common.logger import logger
from django.http import HttpResponse
from fm.databases.database_django import db_get_ordered_missions_multi_type
from fm.models import Mission


def view_test():
    db_missions = Mission.objects.all()
    logger.info('total {}'.format(len(db_missions)))
    logger.info('reput > 0 {}'.format(len(db_missions.filter(reputation_per_hour__gt=0))))
    logger.info('reput > 0 {}'.format(len(db_missions.filter(reputation_per_hour__gte=5))))
    dm_missions = db_missions.filter(reputation_per_hour__gte=5)
    filtered = []
    for i in dm_missions:
        if i.mission_type == '4' and i.km_nb < 2250:
            filtered.append(i)
        elif i.mission_type == '5' and i.km_nb < 11019/2:
            filtered.append(i)
    logger.info('hello {}'.format(len(filtered)))



#     # TODO should read origin_country
#     results = []
#     missions = Mission.objects.all().filter(mission_type='4').filter(reputation_per_hour__gte=0).order_by(criteria)
#     for i in missions:
#         if i.km_nb <= speed and i.travellers_nb <= capacity:
#             results.append(i)
#     return results[:nb_returned_missions]
#
#
# def db_get_ordered_missions_multi_type(nb_returned_missions, criteria):
#     missions = Mission.objects.all().filter(reputation_per_hour__gt=0).order_by(criteria)
#     # missions = filter_impossible_missions(missions)
#     return missions[:nb_returned_missions]
