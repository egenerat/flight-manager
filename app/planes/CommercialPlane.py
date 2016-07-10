from app.common.target_urls import BUY_COMMERCIAL_URL
from app.planes.RootPlane import RootPlane


class CommercialPlane(RootPlane):

    limit_change_engines = 50
    engines_nb = 2
    replacement_engines_type = '4'
    price = 1350000
    buy_url = BUY_COMMERCIAL_URL

    def __init__(self, **kwargs):
        super(CommercialPlane, self).__init__(**kwargs)


    @classmethod
    def get_plane_range(cls):
        return 23000

    @classmethod
    def get_plane_capacity(cls):
        return 440