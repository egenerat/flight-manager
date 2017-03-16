# -*- coding: utf-8 -*-

from abc import ABCMeta
from app.planes.planes_util import get_plane_value


class RootPlane(object):

    def __init__(self, **kwargs):
        __metaclass__ = ABCMeta
        mandatory_fields = ('plane_id', 'ready')
        for field in mandatory_fields:
            setattr(self, field, kwargs.pop(field))
        self.required_maintenance = kwargs.pop('required_maintenance', False)
        self.endlife = kwargs.pop('endlife', False)

        usable_plane_fields = ('kerosene', 'current_engine_hours', 'km')
        if usable_plane_fields[0] in kwargs:
            self.is_usable = True
            for field in usable_plane_fields:
                setattr(self, field, kwargs.pop(field))
            self.km = int(self.km)
            self.current_engine_hours = int(self.current_engine_hours)
        # Usable Jet and Supersonic don't need to specify maximum_engine_hours as it is fixed
        if 'maximum_engine_hours' in kwargs:
            self.maximum_engine_hours = int(self.maximum_engine_hours)

    def engines_to_be_changed(self):
        if self.current_engine_hours and self.limit_change_engines:
            return self.current_engine_hours > self.limit_change_engines
        return False

    def get_value(self):
        if self.km and self.kerosene:
            return get_plane_value(self.new_plane_value, self.km, self.kerosene)

    def get_fuel_consumption_per_hour(self):
        if self.consumption_per_hour:
            return self.consumption_per_hour

    def is_fuel_full(self):
        if self.kerosene and self.fuel_capacity:
            return self.kerosene == self.fuel_capacity

    def __str__(self):
        if self.current_engine_hours and self.maximum_engine_hours:
            return 'Plane {} {}/{}'.format(self.plane_id, self.current_engine_hours, self.maximum_engine_hours)
        else:
            return 'Plane {}'.format(self.plane_id)
