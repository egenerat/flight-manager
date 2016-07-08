from app.planes.JetPlane import JetPlane
from app.planes.UsablePlane import UsablePlane


class UsableJetPlane(JetPlane, UsablePlane):

    def __init__(self, **kwargs):
        kwargs['maximum_engine_hours'] = self.maximum_engine_hours
        for base in UsableJetPlane.__bases__:
            base.__init__(self, **kwargs)
