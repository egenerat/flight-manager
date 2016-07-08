from app.planes.RootPlane import RootPlane


class CommercialPlane(RootPlane):

    limit_change_engines = 50
    engines_nb = 2
    replacement_engines_type = '4'

    def __init__(self, **kwargs):
        super(CommercialPlane, self).__init__(**kwargs)


    @classmethod
    def get_plane_range(cls):
        return 23000

    @classmethod
    def get_plane_capacity(cls):
        return 440