from app.airport.airports_methods import get_other_airports_id, filter_airports, switch_to_airport
from app.manager.bot_player import BotPlayer
from fm.databases.database_django import db_get_ordered_missions_multi_type
from fm.singleton_session import set_airport


class MultiAirportBot(object):
    def __init__(self):
        self.missions = self.get_missions()

    def start(self):
        other_airports = get_other_airports_id()
        other_airports = filter_airports(other_airports)
        for airport_id in other_airports:
            switch_to_airport(airport_id)
            BotPlayer(self.missions).launch_missions()
            #
            # current_airport = Airport()
            # set_airport(current_airport)
            # current_airport.check()


    def get_missions(self):
        db_missions = db_get_ordered_missions_multi_type(210, '-reputation_per_hour')
        # if len(list_missions) < 84 or are_missions_expired(list_missions):
        #     logger.error('Refresh missions')
        #     update_missions()
        #     list_missions = db_get_ordered_missions('Suisse', CONCORDE_SPEED, CONCORDE_CAPACITY, MAX_PLANES_NB,
        #                                             '-reputation_per_hour')
        # if are_expired(db_missions)
        return db_missions

    #         engines_nb_stock = current_airport.get_engines_supply()
    #         engines_nb = get_engines_nb_to_change(ready_planes)
    #         engines_to_buy = engines_nb - engines_nb_stock
    #         if engines_to_buy > 0:
    #             try:
    #                 current_airport.buy_engines(engines_nb - engines_nb_stock)
    #             except:
    #                 logger.error('Could not buy engines')
    #
    #
    #         # TODO: move fill kerozene to check airport? in any case out of bot_player
    #         capacity = current_airport.get_kerozene_capacity()
    #         stock = current_airport.get_kerozene_supply()
    #         difference = capacity - stock
    #         percentage_fuel = math.ceil((stock / float(capacity)) * 100)
    #         if percentage_fuel < 70:
    #             try:
    #                 current_airport.buy_kerozene(difference)
    #             except:
    #                 logger.warning("Couldn't buy kerozene")
    #                 # not working because the money is < 0
    #                 money = current_airport.get_money()
    #                 if money > 0:
    #                     kerozene_litres = int(money / KEROZENE_PRICE)
    #                     logger.info('trying to buy ' + str(kerozene_litres) + ' of kerozene')
    #                     try:
    #                         current_airport.buy_kerozene(kerozene_litres)
    #                     except:
    #                         logger.error("Really can't buy kerozene")
    # force_save_session_to_db()