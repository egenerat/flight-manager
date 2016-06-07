from app.planes.PlaneBean import PlaneBean


class CommercialPlane(PlaneBean):

    limit_change_engine = 40

    def __init__(self, plane_id, required_maintenance, status, kerozene=None, current_engine_hours=None, maximum_engine_hours=None, km=None):
        super(CommercialPlane, self).__init__(plane_id, required_maintenance, status, kerozene, current_engine_hours, maximum_engine_hours, km)
