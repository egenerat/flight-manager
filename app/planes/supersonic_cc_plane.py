# coding=utf-8

from app.common.target_urls import SHOP_CC_ID
from app.planes.supersonic_plane import SupersonicPlane


class SupersonicCCPlane(SupersonicPlane):

    fuel_capacity = 119500
    consumption_per_hour = 25625
    speed = 2250
    plane_range = 2 * speed
    plane_range_stopover = 3 * speed
    minimum_kerosene_before_mission = fuel_capacity
    price = 12590000
    shop_plane_type = SHOP_CC_ID
    plane_capacity = 100

    def __init__(self, **kwargs):
        super(SupersonicCCPlane, self).__init__(**kwargs)
