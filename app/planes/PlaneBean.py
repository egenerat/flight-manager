import abc
from abc import ABCMeta


class PlaneBean:
    __metaclass__ = ABCMeta

    def __init__(self, plane_id, required_maintenance, ready=False, kerozene=None, current_engine_hours=None, km=None):
        self.__plane_id = plane_id
        self.__ready = ready
        self.__required_maintenance = required_maintenance
        self.__kerozene = kerozene
        self.__km = int(km)
        if current_engine_hours:
            self.__current_engine_hours = int(current_engine_hours)

    @abc.abstractmethod
    def is_required_maintenance(self):
        return self.__required_maintenance

    def get_plane_id(self):
        return self.__plane_id

    @abc.abstractmethod
    def engines_to_be_changed(self):
        pass

    def get_status(self):
        return self.__ready

    def __str__(self):
        return 'Plane ' + str(self.__plane_id) + ' ' + str(self.__ready) + ' ' + str(self.__full_fuel) + ' ' + str(
            self.__current_engine_hours)

    @abc.abstractmethod
    def get_value(self):
        pass