# coding=utf-8

from app.common.target_urls import SHOP_COMMERCIAL_8_ID
from app.planes.commercial_plane import CommercialPlane


class Commercial8Plane4(CommercialPlane):
    # config with type 4 engines
    engines_nb = 4
    consumption_per_hour = 15470
    fuel_capacity = 325000
    minimum_kerosene_before_mission = fuel_capacity
    price = 3700000
    shop_plane_type = SHOP_COMMERCIAL_8_ID
    plane_capacity = 853
    plane_range = 13608
    plane_range_stopover = 20412
    speed = 1134

    def __init__(self, **kwargs):
        super(Commercial8Plane4, self).__init__(**kwargs)
