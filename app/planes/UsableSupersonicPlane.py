from app.planes.UsablePlane import ReadyPlane
from app.planes.SupersonicPlane import SupersonicPlane


class ReadySupersonicPlane(SupersonicPlane, ReadyPlane):

    def __init__(self, **kwargs):
        kwargs['maximum_engine_hours'] = self.maximum_engine_hours
        for base in ReadySupersonicPlane.__bases__:
            base.__init__(self, **kwargs)
