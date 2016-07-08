from app.planes.JetPlane import JetPlane
from app.planes.UsablePlane import ReadyPlane


class ReadyJetPlane(JetPlane, ReadyPlane):

    def __init__(self, **kwargs):
        kwargs['maximum_engine_hours'] = self.maximum_engine_hours
        for base in ReadyJetPlane.__bases__:
            base.__init__(self, **kwargs)
