# coding=utf-8

class AirportConfig(object):
    def __init__(self, commercials_nb=0, jets_nb=0, supersonics_nb=0):
        self.commercials_nb = commercials_nb
        self.jets_nb = jets_nb
        self.supersonics_nb = supersonics_nb
        #
        # self.kerozene =


def airport_config_factory(airport_capacity):
    return {
        3: AirportConfig(supersonics_nb=3),
        9: AirportConfig(supersonics_nb=7, jets_nb=2),
        18: AirportConfig(supersonics_nb=14, jets_nb=4),
        27: AirportConfig(supersonics_nb=16, jets_nb=11),
        36: AirportConfig(supersonics_nb=19, jets_nb=17),
        54: AirportConfig(supersonics_nb=24, jets_nb=30),
        84: AirportConfig(supersonics_nb=30, jets_nb=54),
        114: AirportConfig(supersonics_nb=43, jets_nb=71),
        # theory supersonics_nb=64, jets_nb=136
        # in practice, with 2 planes at the same time on the same mission
        200: AirportConfig(supersonics_nb=60, jets_nb=140),
    }[airport_capacity]


class StaffConfig(object):
    def __init__(self, pilots_nb, flight_attendants_nb, mechanics):
        self.pilots_nb = pilots_nb
        self.flight_attendants_nb = flight_attendants_nb
        self.mechanics = mechanics
        # TODO calculate automatically radar watcher and security guys


class ResourcesConfig(object):
    # todo this class should be auto completed
    def __init__(self, airport_config):
        self.kerosene = airport_config.jets_nb * 10000 + airport_config.supersonics_nb * 100000
        self.engines5 = airport_config.jets_nb / 5
        self.engines6 = 12


h3_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h9_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h18_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h27_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h36_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h54_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h84_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h114_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h200_staff_setup = StaffConfig(pilots_nb=430, flight_attendants_nb=260, mechanics=120)


h3_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h9_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h18_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h27_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h36_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h54_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h84_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h114_plane_setup = StaffConfig(pilots_nb=1, flight_attendants_nb=2, mechanics=1)
h200_staff_setup = StaffConfig(pilots_nb=430, flight_attendants_nb=260, mechanics=120)
