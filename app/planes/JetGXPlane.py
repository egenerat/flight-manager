# coding=utf-8
from app.common.target_urls import BUY_JET_GX_URL
from app.planes.JetPlane import JetPlane


class JetGXPlane(JetPlane):

    engines_nb = 2
    consumption_per_hour = 2014
    fuel_capacity = 25382
    minimum_kerosene_before_mission = fuel_capacity
    # 8 (max hours one way) * speed * 2 (2 ways)
    plane_range = 14464
    price = 2650000
    buy_url = BUY_JET_GX_URL
    plane_capacity = 19
    speed = 905

    def __init__(self, **kwargs):
        super(JetGXPlane, self).__init__(**kwargs)
