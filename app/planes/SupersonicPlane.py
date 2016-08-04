# coding=utf-8

from app.common.target_urls import BUY_SUPERSONIC_URL
from app.planes.RootPlane import RootPlane


class SupersonicPlane(RootPlane):

    engines_nb = 4
    limit_change_engines = 97
    maximum_engine_hours = 100
    replacement_engines_type = '6'
    fuel_capacity = 119500
    consumption_per_hour = 25625
    speed = 2250
    plane_range = 2*speed
    minimum_kerosene_before_mission = 70000
    price = 12590000
    buy_url = BUY_SUPERSONIC_URL
    plane_capacity = 100

    def __init__(self, **kwargs):
        super(SupersonicPlane, self).__init__(**kwargs)
