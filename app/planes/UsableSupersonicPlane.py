from app.planes.UsablePlane import UsablePlane
from app.planes.SupersonicPlane import SupersonicPlane


class UsableSupersonicPlane(SupersonicPlane, UsablePlane):

    def __init__(self, **kwargs):
        kwargs['maximum_engine_hours'] = self.maximum_engine_hours
        for base in UsableSupersonicPlane.__bases__:
            base.__init__(self, **kwargs)
