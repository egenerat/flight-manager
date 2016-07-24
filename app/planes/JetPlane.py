from app.common.target_urls import BUY_JET_URL
from app.planes.RootPlane import RootPlane


class JetPlane(RootPlane):

    engines_nb = 3
    limit_change_engines = 63
    maximum_engine_hours = 75
    replacement_engines_type = '5'
    consumption_per_hour = 1510
    fuel_capacity = 18050
    minimum_kerosene_before_mission = fuel_capacity
    plane_range = 11019
    price = 2390000
    buy_url = BUY_JET_URL

    def __init__(self, **kwargs):
        super(JetPlane, self).__init__(**kwargs)

    @classmethod
    def get_plane_range(cls):
        return cls.plane_range

    @classmethod
    def get_plane_capacity(cls):
        return 19
