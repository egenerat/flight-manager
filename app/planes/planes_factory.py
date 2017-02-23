# coding=utf-8
from app.common.target_parse_strings import JET_F7X, JET_GX, JET_GS, SUPERSONIC_CC, SUPERSONIC_TU, COMMERCIAL_7
from app.planes.jet_gs_plane import JetGSPlane
from app.planes.commercial7plane4 import Commercial7Plane4
from app.planes.jet_ds_plane import JetDSPlane
from app.planes.jet_gx_plane import JetGXPlane
from app.planes.supersonic_cc_plane import SupersonicCCPlane
from app.planes.supersonic_tu_plane import SupersonicTUPlane


def planes_factory(plane_model):
    plane_type = {
        COMMERCIAL_7: Commercial7Plane4,
        JET_F7X: JetDSPlane,
        JET_GX: JetGXPlane,
        JET_GS: JetGSPlane,
        SUPERSONIC_CC: SupersonicCCPlane,
        SUPERSONIC_TU: SupersonicTUPlane,
    }.get(plane_model, None)
    if not plane_type:
        raise NotImplementedError
    return plane_type
