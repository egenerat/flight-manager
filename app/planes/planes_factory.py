# coding=utf-8
from app.common.target_parse_strings import JET_F7X, JET_GX, JET_GS, SUPERSONIC_CC, SUPERSONIC_TU
from app.planes.JetDSPlane import JetDSPlane
from app.planes.JetGXPlane import JetGXPlane
from app.planes.SupersonicCCPlane import SupersonicCCPlane
from app.planes.SupersonicTUPlane import SupersonicTUPlane


def planes_factory(plane_model):
    return {
        JET_F7X: JetDSPlane,
        JET_GX: JetGXPlane,
        JET_GS: JetGXPlane,
        SUPERSONIC_CC: SupersonicCCPlane,
        SUPERSONIC_TU: SupersonicTUPlane,
    }.get(plane_model, NotImplementedError)
