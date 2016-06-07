from app.common.constants import CHANGE_HOUR_SUPERSONIC
from app.planes.PlaneBean import PlaneBean


class SupersonicPlane(PlaneBean):

    limit_change_engines = 96
    engines_nb = 4

    def __init__(self, id, required_maintenance, status, kerozene=None, current_engine_hours=None, maximum_engine_hours=None, km=None):
        super(SupersonicPlane, self).__init__(id, required_maintenance, status, kerozene, current_engine_hours, maximum_engine_hours, km)

    def is_required_maintenance(self):
        pass

    def engines_to_be_changed(self):
        return self.__current_engine_hours >= CHANGE_HOUR_SUPERSONIC
