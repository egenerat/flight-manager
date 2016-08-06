# coding=utf-8

from app.airport.airports_methods import get_other_airports_id, filter_airports, switch_to_airport
from app.manager.bot_player import BotPlayer
from fm.databases.database_django import db_get_ordered_missions_multi_type


class MultiAirportBot(object):
    def __init__(self):
        self.missions = self.get_missions()

    def start(self):
        other_airports = get_other_airports_id()
        other_airports = filter_airports(other_airports)
        # TODO mock
        # other_airports = ['122791']
        for airport_id in other_airports:
            switch_to_airport(airport_id)
            BotPlayer(self.missions).launch_missions()
            #
            # current_airport = Airport()
            # set_airport(current_airport)
            # current_airport.check()

    #TODO
    def get_missions(self):
        db_missions = db_get_ordered_missions_multi_type(210, '-reputation_per_hour')
        # if len(list_missions) < 84 or are_missions_expired(list_missions):
        #     logger.error('Refresh missions')
        #     update_missions()
        #     list_missions = db_get_ordered_missions('Suisse', CONCORDE_SPEED, CONCORDE_CAPACITY, MAX_PLANES_NB,
        #                                             '-reputation_per_hour')
        # if are_expired(db_missions)
        return db_missions
