# coding=utf-8
from app.common.target_parse_strings import JET_F7X, JET_GX, JET_GS, SUPERSONIC_CC, SUPERSONIC_TU, COMMERCIAL_7
from app.planes.Commercial7Plane import Commercial7Plane
from app.planes.JetDSPlane import JetDSPlane
from app.planes.JetGXPlane import JetGXPlane
from app.planes.SupersonicCCPlane import SupersonicCCPlane
from app.planes.SupersonicTUPlane import SupersonicTUPlane


def planes_factory(plane_model):
    plane_type = {
        COMMERCIAL_7: Commercial7Plane,
        JET_F7X: JetDSPlane,
        JET_GX: JetGXPlane,
        JET_GS: JetGXPlane,
        SUPERSONIC_CC: SupersonicCCPlane,
        SUPERSONIC_TU: SupersonicTUPlane,
    }.get(plane_model, None)
    if not plane_type:
        raise NotImplementedError
    return plane_type
