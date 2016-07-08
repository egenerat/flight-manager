from app.common.constants import CHANGE_HOUR_SUPERSONIC
from app.planes.RootPlane import RootPlane


class SupersonicPlane(RootPlane):

    limit_change_engines = 96
    engines_nb = 4
    consumption_per_hour = 25625
    plane_range = 2*2430 #2*2250
    maximum_engine_hours = 100
    replacement_engines_type = '6'

    def __init__(self, **kwargs):
        super(SupersonicPlane, self).__init__(**kwargs)

    @classmethod
    def get_plane_range(cls):
        return cls.plane_range

    @classmethod
    def get_plane_capacity(cls):
        return 140 #100


