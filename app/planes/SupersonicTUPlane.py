# coding=utf-8
from app.common.target_urls import SHOP_TU_ID
from app.planes.SupersonicPlane import SupersonicPlane


class SupersonicTUPlane(SupersonicPlane):

    fuel_capacity = 112300
    consumption_per_hour = 26180
    speed = 2430
    plane_range = 2 * speed
    plane_range_stopover = 3 * speed
    minimum_kerosene_before_mission = fuel_capacity
    price = 14285000
    shop_plane_type = SHOP_TU_ID
    plane_capacity = 140

    def __init__(self, **kwargs):
        super(SupersonicTUPlane, self).__init__(**kwargs)
