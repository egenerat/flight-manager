from app.airport.airport_builder import build_airport
from app.common.http_methods import get_request
from app.common.target_urls import STAFF_PAGE, AIRPORT_PAGE, MISSION_DASHBOARD, PLANES_PAGE
from app.missions.missionparser import get_ongoing_missions, subtract
from app.parsers.planesparser import build_planes_from_html
from app.planes.plane_garage import PlaneGarage
from app.planes.planes_util2 import split_planes_list_by_type
from fm.databases.database import sort_missions_by_type, db_get_ordered_missions_multi_type
from fm.mission_handler import accept_all_missions


class BotPlayer(object):
    def __init__(self):
        self.airport = self.build_airport()
        self.planes = self.build_planes()
        self.ongoing_missions = self.get_ongoing_missions()
        # TODO move sessions retrieval to the upper class
        self.missions = self.get_missions()

    def build_airport(self):
        staff_page = get_request(STAFF_PAGE)
        airport_page = get_request(AIRPORT_PAGE)
        return build_airport(airport_page, staff_page)

    def build_planes(self):
        html_page = get_request(PLANES_PAGE)
        planes_list = build_planes_from_html(html_page)
        sorted_planes = split_planes_list_by_type(planes_list)
        return sorted_planes

    def get_ongoing_missions(self):
        dashboard = get_request(MISSION_DASHBOARD)
        return get_ongoing_missions(dashboard)

    def get_missions(self):
        return db_get_ordered_missions_multi_type(200, '-reputation_per_hour')

    @property
    def usable_planes(self):
        return self.planes['commercial_ready_planes'] + self.planes['supersonic_ready_planes'] + self.planes['jet_ready_planes']

    def launch_missions(self):
        mission_list = self.missions
        ongoing_missions = self.ongoing_missions
        mission_list = subtract(mission_list, ongoing_missions)
        garage = PlaneGarage(self.usable_planes, self.airport)
        garage.prepare_all_planes()
        accept_all_missions(mission_list, garage.ready_planes)



###################################################



    def are_missions_expired(missions):
        # TODO improve environment handling
        if fm.singleton_session.local_mode:
            return False
        expiry_date = missions[0].expiry_date
        today = datetime.datetime.now()
        return (expiry_date - today) <= datetime.timedelta(0)



def send_planes():
    list_missions = db_get_ordered_missions('Suisse', CONCORDE_SPEED, CONCORDE_CAPACITY, MAX_PLANES_NB,
                                            '-reputation_per_hour')

    other_airports = get_other_airports_id()
    other_airports = filter_airports(other_airports)

    if len(list_missions) < 84 or are_missions_expired(list_missions):
        logger.error('Refresh missions')
        update_missions()
        list_missions = db_get_ordered_missions('Suisse', CONCORDE_SPEED, CONCORDE_CAPACITY, MAX_PLANES_NB,
                                                '-reputation_per_hour')

    # switch on all airports
    for j in other_airports:
        switch_to_airport(j)

        current_airport = Airport()

        logger.info('Airport : ' + j + ' ' + current_airport.get_airport_name())

        set_airport(current_airport)
        current_airport.check()

        if current_airport.get_planes_nb() > 0:
            # Build planes
            page = get_request()
            ready_planes = build_planes_from_html(page)

            engines_nb_stock = current_airport.get_engines_supply()
            engines_nb = get_engines_nb_to_change(ready_planes)
            engines_to_buy = engines_nb - engines_nb_stock
            if engines_to_buy > 0:
                try:
                    current_airport.buy_engines(engines_nb - engines_nb_stock)
                except:
                    logger.error('Could not buy engines')
            # Prepare all planes
            temp = []

            try:
                for i in ready_planes:
                    i.prepare_for_mission()
                    if i.get_status():
                        temp.append(i)
            except OutdatedPlanesListException:
                page = get_request()
                ready_planes = build_planes_from_html(page)

                engines_nb_stock = current_airport.get_engines_supply()
                engines_nb = get_engines_nb_to_change(ready_planes)
                engines_to_buy = engines_nb - engines_nb_stock
                if engines_to_buy > 0:
                    try:
                        current_airport.buy_engines(engines_nb - engines_nb_stock)
                    except:
                        logger.error('Could not buy engines')
                # Prepare all planes
                temp = []
                for i in ready_planes:
                    i.prepare_for_mission()
                    if i.get_status():
                        temp.append(i)

            ready_planes = temp

            ready_planes_nb = len(ready_planes)

            # TODO: move fill kerozene to check airport? in any case out of bot_player
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
    force_save_session_to_db()
