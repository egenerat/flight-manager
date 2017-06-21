# -*- coding: utf-8 -*-

from app.airport.airport_config import AirportConfig
from app.common.constants import MAIN_AIRPORT_NAME
from app.common.constants_strategy import JET_MODEL_TO_BE_PURCHASED, COMMERCIAL_MODEL_TO_BE_PURCHASED, \
    SUPERSONIC_MODEL_TO_BE_PURCHASED
from app.planes.plane_maintainer import take_planes_alliance
from app.planes.planes_util2 import get_planes_nb_from_sorted_dict


class AirportChecker(object):
    def __init__(self, airport, sorted_planes_dict, injected_airport_buyer, injected_staff_buyer):
        self.airport = airport
        self.sorted_planes_dict = sorted_planes_dict
        self.airport_config = AirportConfig(self.airport)
        self.airport_buyer = injected_airport_buyer
        self.injected_staff_buyer = injected_staff_buyer
        self.refresh_needed = False

    def check_missing_planes(self):
        config = self.airport_config.planes_config
        return {
            COMMERCIAL_MODEL_TO_BE_PURCHASED: config.commercials_nb - len(self.sorted_planes_dict['commercial_planes']),
            JET_MODEL_TO_BE_PURCHASED: config.jets_nb - len(self.sorted_planes_dict['jet_planes']),
            SUPERSONIC_MODEL_TO_BE_PURCHASED: config.supersonics_nb - len(self.sorted_planes_dict['supersonic_planes']),
        }

    def fix_missing_planes(self):
        total_missing_planes = self.airport.planes_capacity - get_planes_nb_from_sorted_dict(self.sorted_planes_dict)
        if total_missing_planes > 0:
            self.refresh_needed = True
            if self.airport.airport_name == MAIN_AIRPORT_NAME:
                for plane_class, missing_units in self.check_missing_planes().iteritems():
                    if missing_units > 0:
                        self.airport_buyer.buy_missing_planes(plane_class, min(missing_units, total_missing_planes))
                        # TODO new_planes var should be set with the result of buying_missing_planes
            else:
                take_planes_alliance(total_missing_planes)

    def fix_missing_staff(self):
        current_staff = self.airport.staff
        staff_config = self.airport_config.staff_config
        pilots_diff = staff_config.pilots_nb - current_staff.total_pilots
        if pilots_diff > 0:
            self.injected_staff_buyer.hire_pilots(pilots_diff)
        flight_attendants_diff = staff_config.flight_attendants_nb - current_staff.total_flight_attendants
        if flight_attendants_diff > 0:
            self.injected_staff_buyer.hire_flight_attendants(flight_attendants_diff)
        mechanics_diff = staff_config.mechanics_nb - current_staff.total_mechanics
        if mechanics_diff > 0:
            self.injected_staff_buyer.hire_mechanics(mechanics_diff)

    def fix_missing_resources(self):
        kerosene_config = self.airport_config.resources_config.kerosene
        if self.airport.kerosene_supply < kerosene_config['min']:
            qty_needed = kerosene_config['max'] - self.airport.kerosene_supply
            self.airport_buyer.buy_kerosene(qty_needed)
        engines_5_nb = self.airport_config.resources_config.engines_5_nb
        if self.airport.engines_supply['5'] < engines_5_nb['min']:
            qty_needed = engines_5_nb['max'] - self.airport.engines_supply['5']
            self.airport_buyer.buy_engines(qty_needed, '5')
        engines_6_nb = self.airport_config.resources_config.engines_6_nb
        if self.airport.engines_supply['6'] < engines_6_nb['min']:
            qty_needed = engines_6_nb['max'] - self.airport.engines_supply['6']
            self.airport_buyer.buy_engines(qty_needed, '6')

    def fix(self):
        self.fix_missing_planes()
        self.fix_missing_staff()
        self.fix_missing_resources()
