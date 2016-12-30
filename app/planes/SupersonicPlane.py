# coding=utf-8
from abc import ABCMeta

from app.planes.RootPlane import RootPlane


class SupersonicPlane(RootPlane):

    engines_nb = 4
    limit_change_engines = 95
    maximum_engine_hours = 100
    replacement_engines_type = '6'

    def __init__(self, **kwargs):
        __metaclass__ = ABCMeta
        super(SupersonicPlane, self).__init__(**kwargs)
