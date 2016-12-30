# coding=utf-8
from abc import ABCMeta

from app.common.target_urls import BUY_JET_DS_URL
from app.planes.RootPlane import RootPlane


class JetPlane(RootPlane):

    limit_change_engines = 61
    maximum_engine_hours = 75
    replacement_engines_type = '5'

    def __init__(self, **kwargs):
        __metaclass__ = ABCMeta
        super(JetPlane, self).__init__(**kwargs)
