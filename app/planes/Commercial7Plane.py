# coding=utf-8

from app.common.target_urls import BUY_COMMERCIAL_URL
from app.planes.CommercialPlane import CommercialPlane


class Commercial7Plane(CommercialPlane):
    engines_nb = 2
    consumption_per_hour = 7007
    fuel_capacity = 171170
    minimum_kerosene_before_mission = fuel_capacity
    price = 1350000
    buy_url = BUY_COMMERCIAL_URL
    plane_capacity = 440
    plane_range = 23721
    speed = 971

    def __init__(self, **kwargs):
        super(Commercial7Plane, self).__init__(**kwargs)
