# coding=utf-8

from app.planes.RootPlane import RootPlane


class SupersonicPlane(RootPlane):

    engines_nb = 4
    limit_change_engines = 97
    maximum_engine_hours = 100
    replacement_engines_type = '6'

    def __init__(self, **kwargs):
        super(SupersonicPlane, self).__init__(**kwargs)
