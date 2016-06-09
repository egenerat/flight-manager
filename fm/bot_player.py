# -*- coding: utf-8 -*-

import datetime
import math

from app.airport.Airport import Airport
from app.airport.airports_methods import get_other_airports_id, \
    switch_to_airport, filter_airports
from app.common.as_exceptions import OutdatedPlanesListException
from app.common.constants import PLANES_PAGE, CONCORDE_SPEED, CONCORDE_CAPACITY, \
    KEROZENE_PRICE, MAX_PLANES_NB
from app.common.countries import countries
from app.common.file_methods import force_save_session_to_db
from app.common.http_methods import get_request
from app.common.logger import logger
from app.missions.mission import get_ongoing_missions, subtract, \
    accept_all_missions, list_missions, get_real_benefit, get_expiry_date
from app.planes.deserialization import build_planes_from_html
from fm.models import Mission
from fm.singleton_session import set_airport
import fm.singleton_session
from fm.database import db_remove_all_missions, db_insert_object, db_get_ordered_missions


def are_missions_expired(missions):
    #TODO improve environment handling
    if fm.singleton_session.local_mode:
        return False
    expiry_date = missions[0].expiry_date
    today = datetime.datetime.now()
    return (expiry_date - today) <= datetime.timedelta(0)


def analyse_missions():
    # Be careful, if all airports are in the same country, lot of redundancy
    db_remove_all_missions()
    other_airports = ["131469"]#get_other_airports_id()
    for j in other_airports:
        # remove duplicates (airports in the same country)
        #if j != '125146':
        switch_to_airport(j)
        current_airport = Airport()
        country = current_airport.get_country()
        logger.error(j + ' : ' + country)
        missions_list = list_missions()
        for a_mission_dict in missions_list:
            a_mission = Mission(**a_mission_dict)
            a_mission.expiry_date = get_expiry_date()
            a_mission.revenue_per_hour = get_real_benefit(a_mission)
            a_mission.origin_country = country
            total_hours = a_mission.time_before_departure + math.ceil(a_mission.km_nb / CONCORDE_SPEED) * 2
            a_mission.total_time = total_hours
            a_mission.reputation_per_hour = int(int(a_mission.reputation) / total_hours)
            db_insert_object(a_mission)
    return None


def update_missions():
    switch_to_airport("131469")
    db_remove_all_missions()
    missions_list = list_missions()
    current_airport = Airport()
    country = current_airport.get_country()
    expiry_date = get_expiry_date()
    for a_mission_dict in missions_list:
        a_mission = Mission(**a_mission_dict)
        a_mission.expiry_date = expiry_date.replace(tzinfo=None)
        a_mission.revenue_per_hour = get_real_benefit(a_mission)
        a_mission.origin_country = country
        total_hours = int(a_mission.time_before_departure + math.ceil(a_mission.km_nb / CONCORDE_SPEED) * 2)
        a_mission.total_time = total_hours
        a_mission.reputation_per_hour = int(int(a_mission.reputation) / total_hours)
        db_insert_object(a_mission)


def get_engines_nb_to_change(plane_list):
    result = 0
    for i in plane_list:
        if i.get_status() and i.engines_to_be_changed():
            result += 4
    return result


def send_planes():
    list_missions = db_get_ordered_missions('Suisse', CONCORDE_SPEED, CONCORDE_CAPACITY, MAX_PLANES_NB, '-reputation_per_hour')

    other_airports = get_other_airports_id()
    other_airports = filter_airports(other_airports)

    if len(list_missions) < 84 or are_missions_expired(list_missions):
        logger.error('Refresh missions')
        update_missions()
        list_missions = db_get_ordered_missions('Suisse', CONCORDE_SPEED, CONCORDE_CAPACITY, MAX_PLANES_NB, '-reputation_per_hour')

    # switch on all airports
    for j in other_airports:
        switch_to_airport(j)

        current_airport = Airport()

        logger.info('Airport : ' + j + ' ' + current_airport.get_airport_name())

        set_airport(current_airport)
        current_airport.check()

        if current_airport.get_planes_nb() > 0:
            # Build planes
            page = get_request(PLANES_PAGE)
            ready_planes = build_planes_from_html(page)

            engines_nb_stock = current_airport.get_engines_supply()
            engines_nb = get_engines_nb_to_change(ready_planes)
            engines_to_buy = engines_nb - engines_nb_stock
            if engines_to_buy > 0:
                try:
                    current_airport.buy_engines(engines_nb - engines_nb_stock)
                except:
                    logger.error('Could not buy engines')
            #         Prepare all planes
            temp = []
            
            try:
                for i in ready_planes:
                    i.prepare_for_mission()
                    if i.get_status():
                        temp.append(i)
            except OutdatedPlanesListException:
                page = get_request(PLANES_PAGE)
                ready_planes = build_planes_from_html(page)

                engines_nb_stock = current_airport.get_engines_supply()
                engines_nb = get_engines_nb_to_change(ready_planes)
                engines_to_buy = engines_nb - engines_nb_stock
                if engines_to_buy > 0:
                    try:
                        current_airport.buy_engines(engines_nb - engines_nb_stock)
                    except:
                        logger.error('Could not buy engines')
                #         Prepare all planes
                temp = []
                for i in ready_planes:
                    i.prepare_for_mission()
                    if i.get_status():
                        temp.append(i)

            ready_planes = temp

            ready_planes_nb = len(ready_planes)

            #TODO: move fill kerozene to check airport? in any case out of bot_player
            capacity = current_airport.get_kerozene_capacity()
            stock = current_airport.get_kerozene_supply()
            difference = capacity - stock
            percentage_fuel = math.ceil((stock / float(capacity)) * 100)
            if percentage_fuel < 70:
                try:
                    current_airport.buy_kerozene(difference)
                except:
                    logger.warning("Couldn't buy kerozene")
                    # not working because the money is < 0
                    money = current_airport.get_money()
                    if money > 0:
                        kerozene_litres = int(money / KEROZENE_PRICE)
                        logger.info('trying to buy ' + str(kerozene_litres) + ' of kerozene')
                        try:
                            current_airport.buy_kerozene(kerozene_litres)
                        except:
                            logger.error("Really can't buy kerozene")
            # 1 get all mission ordered
            missions_list = list_missions

            # 2 purge all already ongoing
            ongoing_missions_id = get_ongoing_missions()
            missions_list = subtract(missions_list, ongoing_missions_id)

            # 3 cut just the good number
            missions_list = missions_list[:ready_planes_nb]

            # 4 group missions by country 
            missions_json = {}
            for i in missions_list:
                i.country = countries[str(i.country_nb)]
                if i.country_nb not in missions_json:
                    missions_json[i.country_nb] = []
                missions_json[i.country_nb].append(i.mission_nb)

            # purge empty countries
            result = {}
            for i in missions_json:
                if missions_json[i]:
                    result[i] = missions_json[i]
            accept_all_missions(result, ready_planes)
    force_save_session_to_db()
