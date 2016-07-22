from app.planes.planes_util import get_plane_value
from abc import ABCMeta


class abstractstatic(classmethod):
    __slots__ = ()

    def __init__(self, function):
        super(abstractstatic, self).__init__(function)
        function.__isabstractmethod__ = True

    __isabstractmethod__ = True


class UsablePlane(object):
    __metaclass__ = ABCMeta

    def __init__(self, **kwargs):
        mandatory_fields = ('kerosene', 'current_engine_hours', 'maximum_engine_hours', 'km')
        for field in mandatory_fields:
            setattr(self, field, kwargs.pop(field))
        self.km = int(self.km)
        self.current_engine_hours = int(self.current_engine_hours)
        self.maximum_engine_hours = int(self.maximum_engine_hours)

    def engines_to_be_changed(self):
        return self.current_engine_hours > self.limit_change_engines

    def get_value(self):
        if self.km and self.kerosene:
            return get_plane_value(self.new_plane_value, self.km, self.kerosene)

    def get_fuel_consumption_per_hour(self):
        return self.consumption_per_hour

    def is_fuel_full(self):
        return self.kerosene == self.fuel_capacity

    def __str__(self):
        return 'Plane {} {}/{}'.format(self.plane_id, self.current_engine_hours, self.maximum_engine_hours)

    @abstractstatic
    def get_plane_range(cls):
        pass

    @abstractstatic
    def get_plane_capacity(cls):
        pass
