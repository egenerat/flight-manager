from app.planes.RootPlane import RootPlane
from app.planes.planes_util import get_plane_value


class PlaneBean(RootPlane):

    def __init__(self, id, required_maintenance, status, kerozene=None, current_engine_hours=None, maximum_engine_hours=None, km=None):
        super(PlaneBean, self).__init__(id)
        self.__status = status
        self.__required_maintenance = required_maintenance
        self.__kerozene = int(kerozene) if kerozene else None
        self.__km = int(km) if km else None
        self.__current_engine_hours = int(current_engine_hours) if current_engine_hours else None
        self.__maximum_engine_hours = int(maximum_engine_hours) if maximum_engine_hours else None

    def is_required_maintenance(self):
        return self.__required_maintenance

    def engines_to_be_changed(self):
        return self.__current_engine_hours > self.limit_change_engine

    def get_plane_id(self):
        return self.__plane_id

    def get_status(self):
        return self.__ready

    def get_value(self):
        if self.__km and self.__kerozene:
            return get_plane_value(self.new_plane_value, self.__km, self.__kerozene)

    def __str__(self):
        return 'Plane ' + str(self.__plane_id) + ' ' + str(self.__ready) + ' ' + str(self.__full_fuel) + ' ' + str(
            self.__current_engine_hours)
