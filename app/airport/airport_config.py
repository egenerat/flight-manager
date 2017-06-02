# -*- coding: utf-8 -*-


class AirportConfig(object):
    def __init__(self, airport):
        self.airport = airport
        self.planes_config = planes_config_factory(self.airport.planes_capacity)
        self.staff_config = staff_config_factory(self.airport.planes_capacity)
        self.resources_config = ResourcesConfig(self.airport, self.planes_config)


class PlanesConfig(object):
    def __init__(self, commercials_nb=0, jets_nb=0, supersonics_nb=0):
        self.commercials_nb = commercials_nb
        self.jets_nb = jets_nb
        self.supersonics_nb = supersonics_nb


def planes_config_factory(airport_capacity):
    return {
        3: PlanesConfig(supersonics_nb=3),
        9: PlanesConfig(supersonics_nb=9),
        18: PlanesConfig(supersonics_nb=18),
        27: PlanesConfig(supersonics_nb=27),
        36: PlanesConfig(supersonics_nb=36),
        54: PlanesConfig(supersonics_nb=52, jets_nb=2),
        # 84: PlanesConfig(supersonics_nb=81, jets_nb=3),
        # in order to reduce planes number
        84: PlanesConfig(supersonics_nb=0, jets_nb=30),
        114: PlanesConfig(supersonics_nb=104, jets_nb=110),
        200: PlanesConfig(supersonics_nb=95, jets_nb=105),
    }[airport_capacity]


class StaffConfig(object):
    def __init__(self, pilots_nb, flight_attendants_nb, mechanics_nb):
        self.pilots_nb = pilots_nb
        self.flight_attendants_nb = flight_attendants_nb
        self.mechanics_nb = mechanics_nb
        # TODO calculate automatically radar watcher and security guys


def staff_config_factory(airport_capacity):
    """ should be improved, and be variable of supersonic nb and jets nb """
    return {
        3: StaffConfig(pilots_nb=6, flight_attendants_nb=8, mechanics_nb=8),
        9: StaffConfig(pilots_nb=20, flight_attendants_nb=16, mechanics_nb=16),
        18: StaffConfig(pilots_nb=42, flight_attendants_nb=25, mechanics_nb=16),
        27: StaffConfig(pilots_nb=20, flight_attendants_nb=16, mechanics_nb=16),
        36: StaffConfig(pilots_nb=100, flight_attendants_nb=56, mechanics_nb=32),
        54: StaffConfig(pilots_nb=85, flight_attendants_nb=56, mechanics_nb=32),
        84: StaffConfig(pilots_nb=250, flight_attendants_nb=120, mechanics_nb=40),
        114: StaffConfig(pilots_nb=190, flight_attendants_nb=115, mechanics_nb=40),
        200: StaffConfig(pilots_nb=510, flight_attendants_nb=315, mechanics_nb=200),
    }[airport_capacity]


class ResourcesConfig(object):
    def __init__(self, airport, planes_config):
        # self.kerosene = airport_config.jets_nb * 10000 + airport_config.supersonics_nb * 100000
        # multiple of the airport capacity
        self.kerosene = {
            'min': 0.7*airport.kerosene_capacity,
            'max': 1*airport.kerosene_capacity
        }
        self.engines_5_nb = {
            'min': 3*planes_config.jets_nb/4,
            'max': 3*planes_config.jets_nb/2
        }
        self.engines_6_nb = {
            'min': 4*planes_config.supersonics_nb/10,
            'max': 4*planes_config.supersonics_nb/7
        }
