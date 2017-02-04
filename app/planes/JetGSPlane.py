# coding=utf-8
from app.common.target_urls import SHOP_GS_ID
from app.planes.JetPlane import JetPlane


class JetGSPlane(JetPlane):

    engines_nb = 2
    consumption_per_hour = 1735
    fuel_capacity = 24000
    minimum_kerosene_before_mission = fuel_capacity
    # 8 (max hours one way) * speed * 2 (2 ways)
    plane_range = 7232
    plane_range_stopover = 10848
    price = 2800000
    shop_plane_type = SHOP_GS_ID
    plane_capacity = 19
    speed = 904

    def __init__(self, **kwargs):
        super(JetGSPlane, self).__init__(**kwargs)
