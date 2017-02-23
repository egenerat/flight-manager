# coding=utf-8
from app.common.target_urls import SHOP_GX_ID
from app.planes.jet_plane import JetPlane


class JetGXPlane(JetPlane):

    engines_nb = 2
    consumption_per_hour = 2014
    fuel_capacity = 25382
    minimum_kerosene_before_mission = fuel_capacity
    # 7 (max hours one way) * speed * 2 (2 ways)
    plane_range = 6335
    plane_range_stopover = 9955
    price = 2650000
    shop_plane_type = SHOP_GX_ID
    plane_capacity = 19
    speed = 905

    def __init__(self, **kwargs):
        super(JetGXPlane, self).__init__(**kwargs)
