# coding=utf-8

from app.planes.CommercialPlane import CommercialPlane
from app.planes.JetPlane import JetPlane
from app.planes.UsableCommercialPlane import UsableCommercialPlane
from app.planes.UsableJetPlane import UsableJetPlane
from app.planes.UsableSupersonicPlane import UsableSupersonicPlane
from app.planes.SupersonicPlane import SupersonicPlane


def split_planes_list_by_type(planes_list):
    result = {
        'commercial_planes': [],
        'jet_planes': [],
        'supersonic_planes': [],
        'commercial_ready_planes': [],
        'jet_ready_planes': [],
        'supersonic_ready_planes': [],
    }
    for i in planes_list:
        if isinstance(i, SupersonicPlane):
            result['supersonic_planes'].append(i)
        if isinstance(i, CommercialPlane):
            result['commercial_planes'].append(i)
        if isinstance(i, JetPlane):
            result['jet_planes'].append(i)
        if isinstance(i, UsableSupersonicPlane) and i.ready:
            result['supersonic_ready_planes'].append(i)
        if isinstance(i, UsableCommercialPlane) and i.ready:
            result['commercial_ready_planes'].append(i)
        if isinstance(i, UsableJetPlane) and i.ready:
            result['jet_ready_planes'].append(i)
    return result
