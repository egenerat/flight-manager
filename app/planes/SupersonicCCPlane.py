# coding=utf-8

from app.common.target_urls import BUY_SUPERSONIC_CC_URL
from app.planes.SupersonicPlane import SupersonicPlane


class SupersonicCCPlane(SupersonicPlane):

    fuel_capacity = 119500
    consumption_per_hour = 25625
    speed = 2250
    plane_range = 4 * speed
    minimum_kerosene_before_mission = fuel_capacity
    price = 12590000
    buy_url = BUY_SUPERSONIC_CC_URL
    plane_capacity = 100

    def __init__(self, **kwargs):
        super(SupersonicCCPlane, self).__init__(**kwargs)
