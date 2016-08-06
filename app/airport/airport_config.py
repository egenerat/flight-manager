# coding=utf-8


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
        9: PlanesConfig(supersonics_nb=7, jets_nb=2),
        18: PlanesConfig(supersonics_nb=14, jets_nb=4),
        27: PlanesConfig(supersonics_nb=16, jets_nb=11),
        36: PlanesConfig(supersonics_nb=19, jets_nb=17),
        54: PlanesConfig(supersonics_nb=24, jets_nb=30),
        84: PlanesConfig(supersonics_nb=30, jets_nb=54),
        114: PlanesConfig(supersonics_nb=43, jets_nb=71),
        # theory supersonics_nb=64, jets_nb=136
        # in practice, with 2 planes at the same time on the same mission
        200: PlanesConfig(supersonics_nb=60, jets_nb=140),
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
        # 18: StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1),
        # 27: StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1),
        36: StaffConfig(pilots_nb=72, flight_attendants_nb=66, mechanics_nb=32),
        # 54: StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1),
        84: StaffConfig(pilots_nb=180, flight_attendants_nb=160, mechanics_nb=40),
        # 114: StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1),
        200: StaffConfig(pilots_nb=420, flight_attendants_nb=260, mechanics_nb=120),
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
