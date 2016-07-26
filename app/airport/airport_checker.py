# coding=utf-8

from app.airport.airport_buyer import buy_missing_planes
from app.airport.airport_plane_type_config import airport_config_factory
from app.planes.CommercialPlane import CommercialPlane
from app.planes.JetPlane import JetPlane
from app.planes.SupersonicPlane import SupersonicPlane


def amount_needed(missing_planes):
    amount = 0
    for aircraft_type, missing_units in missing_planes.iteritems():
        amount += missing_units * aircraft_type.price
    return amount


class AirportChecker(object):
    def __init__(self, airport, sorted_planes_dict):
        self.airport = airport
        self.sorted_planes_dict = sorted_planes_dict

    def check_missing_planes(self):
        config = airport_config_factory(self.airport.planes_capacity)
        return {
            CommercialPlane: config.commercials_nb - len(self.sorted_planes_dict['commercial_planes']),
            JetPlane: config.jets_nb - len(self.sorted_planes_dict['jet_planes']),
            SupersonicPlane: config.supersonics_nb - len(self.sorted_planes_dict['supersonic_planes']),
        }

    def fix_missing_planes(self):
        for plane_class, missing_units in self.check_missing_planes().iteritems():
            if self.airport.planes_capacity > len(self.sorted_planes_dict.values()) and missing_units > 0:
                buy_missing_planes(plane_class, missing_units)
