# coding=utf-8

from app.common.target_urls import BUY_JET_DS_URL
from app.planes.JetPlane import JetPlane


class JetDSPlane(JetPlane):

    engines_nb = 3
    consumption_per_hour = 1510
    fuel_capacity = 18050
    minimum_kerosene_before_mission = fuel_capacity
    # 7 (max hours one way) * speed * 2 (2 ways)
    plane_range = 6454
    plane_range_stopover = 10142
    price = 2390000
    buy_url = BUY_JET_DS_URL
    plane_capacity = 19
    speed = 922

    def __init__(self, **kwargs):
        super(JetDSPlane, self).__init__(**kwargs)
