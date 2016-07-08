from app.planes.CommercialPlane import CommercialPlane
from app.planes.UsablePlane import UsablePlane


class UsableCommercialPlane(CommercialPlane, UsablePlane):

    def __init__(self, **kwargs):
        for base in UsableCommercialPlane.__bases__:
            base.__init__(self, **kwargs)

