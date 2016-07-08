from app.planes.CommercialPlane import CommercialPlane
from app.planes.JetPlane import JetPlane
from app.planes.UsableCommercialPlane import UsableCommercialPlane
from app.planes.UsableJetPlane import UsableJetPlane
from app.planes.UsableSupersonicPlane import UsableSupersonicPlane
from app.planes.SupersonicPlane import SupersonicPlane


def is_supersonic(string_model):
    return string_model in [u'Concorde', u'Tu-144']


def is_jet(string_model):
    return string_model in [u'Falcon 7X']


def is_regular_plane(string_model):
    return string_model in [u'B777-200ER']


def usable_planes_factory(plane_model):
    if is_jet(plane_model):
        return UsableJetPlane
    elif is_regular_plane(plane_model):
        return UsableCommercialPlane
    elif is_supersonic(plane_model):
        return UsableSupersonicPlane
    else:
        raise NotImplementedError


def planes_factory(plane_model):
    if is_jet(plane_model):
        return JetPlane
    elif is_regular_plane(plane_model):
        return CommercialPlane
    elif is_supersonic(plane_model):
        return SupersonicPlane
    else:
        raise NotImplementedError
