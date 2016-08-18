# coding=utf-8

from app.airport.airport_buyer import buy_missing_planes, buy_kerosene, buy_engines
from app.airport.airport_config import AirportConfig
from app.airport.staff_buyer import hire_flight_attendants, hire_pilots
from app.airport.staff_buyer import hire_mechanics
from app.planes.CommercialPlane import CommercialPlane
from app.planes.JetPlane import JetPlane
from app.planes.SupersonicPlane import SupersonicPlane
from app.planes.planes_util2 import get_planes_nb_from_sorted_dict


def amount_needed(missing_planes):
    amount = 0
    for aircraft_type, missing_units in missing_planes.iteritems():
        amount += missing_units * aircraft_type.price
    return amount


class AirportChecker(object):
    def __init__(self, airport, sorted_planes_dict):
        self.airport = airport
        self.sorted_planes_dict = sorted_planes_dict
        self.airport_config = AirportConfig(self.airport)

    def check_missing_planes(self):
        config = self.airport_config.planes_config
        return {
            CommercialPlane: config.commercials_nb - len(self.sorted_planes_dict['commercial_planes']),
            JetPlane: config.jets_nb - len(self.sorted_planes_dict['jet_planes']),
            SupersonicPlane: config.supersonics_nb - len(self.sorted_planes_dict['supersonic_planes']),
        }

    def fix_missing_planes(self):
        if self.airport.planes_capacity > get_planes_nb_from_sorted_dict(self.sorted_planes_dict):
            for plane_class, missing_units in self.check_missing_planes().iteritems():
                if missing_units > 0:
                    buy_missing_planes(plane_class, missing_units)

    def fix_missing_staff(self):
        current_staff = self.airport.staff
        staff_config = self.airport_config.staff_config
        pilots_diff = staff_config.pilots_nb - current_staff.total_pilots
        if pilots_diff > 0:
            hire_pilots(pilots_diff)
        flight_attendants_diff = staff_config.flight_attendants_nb - current_staff.total_flight_attendants
        if flight_attendants_diff > 0:
            hire_flight_attendants(flight_attendants_diff)
        mechanics_diff = staff_config.mechanics_nb - current_staff.total_mechanics
        if mechanics_diff > 0:
            hire_mechanics(mechanics_diff)

    def fix_missing_resources(self):
        kerosene_config = self.airport_config.resources_config.kerosene
        if self.airport.kerosene_supply < kerosene_config['min']:
            qty_needed = kerosene_config['max'] - self.airport.kerosene_supply
            buy_kerosene(qty_needed)
        engines_5_nb = self.airport_config.resources_config.engines_5_nb
        if self.airport.engines_supply['5'] < engines_5_nb['min']:
            qty_needed = engines_5_nb['max'] - self.airport.engines_supply['5']
            buy_engines(qty_needed, '5')
        engines_6_nb = self.airport_config.resources_config.engines_6_nb
        if self.airport.engines_supply['6'] < engines_6_nb['min']:
            qty_needed = engines_6_nb['max'] - self.airport.engines_supply['6']
            buy_engines(qty_needed, '6')

    def fix(self):
        self.fix_missing_planes()
        self.fix_missing_staff()
        self.fix_missing_resources()
