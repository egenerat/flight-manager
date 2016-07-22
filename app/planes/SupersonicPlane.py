from app.common.target_urls import BUY_SUPERSONIC_URL
from app.planes.RootPlane import RootPlane


class SupersonicPlane(RootPlane):

    limit_change_engines = 97
    engines_nb = 4
    fuel_capacity = 119500
    consumption_per_hour = 25625
    plane_range = 2*2250
    maximum_engine_hours = 100
    replacement_engines_type = '6'
    price = 12590000
    buy_url = BUY_SUPERSONIC_URL

    def __init__(self, **kwargs):
        super(SupersonicPlane, self).__init__(**kwargs)

    @classmethod
    def get_plane_range(cls):
        return cls.plane_range

    @classmethod
    def get_plane_capacity(cls):
        return 100


