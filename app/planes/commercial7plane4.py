# coding=utf-8

from app.common.target_urls import SHOP_COMMERCIAL_ID
from app.planes.commercial_plane import CommercialPlane


class Commercial7Plane4(CommercialPlane):
    engines_nb = 2
    consumption_per_hour = 7007
    fuel_capacity = 171170
    minimum_kerosene_before_mission = fuel_capacity
    price = 1350000
    shop_plane_type = SHOP_COMMERCIAL_ID
    plane_capacity = 440
    plane_range = 11860
    plane_range_stopover = plane_range
    speed = 971

    def __init__(self, **kwargs):
        super(Commercial7Plane4, self).__init__(**kwargs)
