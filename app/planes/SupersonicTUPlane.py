# coding=utf-8
from app.common.target_urls import BUY_SUPERSONIC_TU_URL
from app.planes.SupersonicPlane import SupersonicPlane


class SupersonicTUPlane(SupersonicPlane):

    fuel_capacity = 112300
    consumption_per_hour = 26180
    speed = 2430
    plane_range = 2 * speed
    plane_range_stopover = plane_range
    minimum_kerosene_before_mission = fuel_capacity
    price = 14285000
    buy_url = BUY_SUPERSONIC_TU_URL
    plane_capacity = 140

    def __init__(self, **kwargs):
        super(SupersonicTUPlane, self).__init__(**kwargs)
