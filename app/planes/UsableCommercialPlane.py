from app.planes.CommercialPlane import CommercialPlane
from app.planes.UsablePlane import ReadyPlane


class ReadyCommercialPlane(CommercialPlane, ReadyPlane):

    def __init__(self, **kwargs):
        for base in ReadyCommercialPlane.__bases__:
            base.__init__(self, **kwargs)

