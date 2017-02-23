# coding=utf-8
from abc import ABCMeta

from app.planes.root_plane import RootPlane


class CommercialPlane(RootPlane):
    limit_change_engines = 50
    # TODO only if engines upgraded
    maximum_engine_hours = 75
    replacement_engines_type = '4'

    def __init__(self, **kwargs):
        __metaclass__ = ABCMeta
        super(CommercialPlane, self).__init__(**kwargs)
