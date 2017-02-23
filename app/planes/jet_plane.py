# coding=utf-8
from abc import ABCMeta

from app.planes.root_plane import RootPlane


class JetPlane(RootPlane):

    # To be reduced further with stopover
    limit_change_engines = 51
    maximum_engine_hours = 75
    replacement_engines_type = '5'

    def __init__(self, **kwargs):
        __metaclass__ = ABCMeta
        super(JetPlane, self).__init__(**kwargs)
