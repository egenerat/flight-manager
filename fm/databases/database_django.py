# -*- coding: utf-8 -*-
import pickle

import fm.singleton_session
from app.missions.mission_utils import is_possible_mission
from fm.models import Mission, AirportsToBeSold, ASHttpSession, Notification, Stopover


def db_remove_all_missions():
    Mission.objects.all().delete()
    Stopover.objects.all().delete()


def db_get_all_missions():
    return Mission.objects.all()


def db_get_all_airports_sold():
    return AirportsToBeSold.objects.all()


def db_remove_all_airports_sold():
    AirportsToBeSold.objects.all().delete()


def db_get_all_notifications():
    return Notification.objects.all()


def remove_all_notifications():
    return Notification.objects.all.delete()


def db_insert_object(obj):
    obj.save()


def db_count_missions():
    return Mission.objects.count()


def filter_missions_analysis(missions):
    result = []
    result_no_commercial = []
    for a_mission in missions:
        if is_possible_mission(a_mission):
            result.append(a_mission)
            if a_mission.mission_type in ["4", "5"]:
                result_no_commercial.append(a_mission)
    return result


def db_get_ordered_missions_multi_type(nb_returned_missions, criteria):
    # TODO should read origin_country
    missions = Mission.objects.all().filter(reputation_per_hour__gt=0).order_by(criteria)
    missions = filter_missions_analysis(missions)
    return missions[:nb_returned_missions]


def read_session_from_db():
    return pickle.loads(ASHttpSession.objects.all()[0].data)


def save_session_to_db():
    session = fm.singleton_session.session_to_server
    ASHttpSession.objects.all().delete()
    a_string = pickle.dumps(session)
    db_session = ASHttpSession()
    db_session.data = a_string
    db_session.save()


def is_session_in_db():
    return ASHttpSession.objects.count() > 0
