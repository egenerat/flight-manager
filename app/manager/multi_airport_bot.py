# -*- coding: utf-8 -*-

from app.airport.airports_methods import switch_to_airport
from app.common.constants import ACTIVE_AIRPORT_ID
from app.common.logger import logger
from app.manager.bot_player import BotPlayer
from fm.databases.database_django import db_get_ordered_missions_multi_type, db_insert_object
from fm.mission_handler import are_missions_expired, parse_all_missions
from fm.models import SupersonicStats


class MultiAirportBot(object):
    def __init__(self):
        self.missions = get_missions()

    def start(self):
        # other_airports = get_other_airports_id()
        # other_airports = filter_airports(other_airports)
        other_airports = ACTIVE_AIRPORT_ID
        for airport_id in other_airports:
            switch_to_airport(airport_id)
            bot = BotPlayer(self.missions)
            logger.info(bot.airport)
            bot.launch_missions()
            # TODO: Should be a while, but be careful with infinite loop
            if bot.refresh_needed:
                bot.launch_missions()
            # Disable email notification for plane crashes
            # bot.check_report()

            stats_dict = bot.stats_supersonics()
            stats = SupersonicStats(**stats_dict)
            db_insert_object(stats)


def get_missions():
    db_missions = db_get_ordered_missions_multi_type(200, '-reputation_per_hour')
    if len(db_missions) < 200 or are_missions_expired(db_missions):
        logger.warning('Refresh missions')
        parse_all_missions()
        db_missions = db_get_ordered_missions_multi_type(200, '-reputation_per_hour')
    return db_missions
