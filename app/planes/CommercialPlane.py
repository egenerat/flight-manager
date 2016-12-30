# coding=utf-8

from app.common.target_urls import BUY_COMMERCIAL_URL
from app.planes.RootPlane import RootPlane


class CommercialPlane(RootPlane):
    engines_nb = 2
    limit_change_engines = 50
    # TODO only if engines upgraded
    maximum_engine_hours = 75
    consumption_per_hour = 7007
    fuel_capacity = 171170
    minimum_kerosene_before_mission = fuel_capacity
    replacement_engines_type = '4'
    price = 1350000
    buy_url = BUY_COMMERCIAL_URL
    plane_capacity = 440
    plane_range = 23721
    speed = 971

    def __init__(self, **kwargs):
        super(CommercialPlane, self).__init__(**kwargs)
