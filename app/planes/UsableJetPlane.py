# coding=utf-8
from app.planes.JetDSPlane import JetDSPlane
from app.planes.UsablePlane import UsablePlane


class UsableJetPlane(JetDSPlane, UsablePlane):

    def __init__(self, **kwargs):
        kwargs['maximum_engine_hours'] = self.maximum_engine_hours
        for base in UsableJetPlane.__bases__:
            base.__init__(self, **kwargs)
