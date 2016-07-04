from app.planes.CommercialPlane import CommercialPlane
from app.planes.JetPlane import JetPlane
from app.planes.ReadyCommercialPlane import ReadyCommercialPlane
from app.planes.ReadyJetPlane import ReadyJetPlane
from app.planes.ReadySupersonicPlane import ReadySupersonicPlane
from app.planes.SupersonicPlane import SupersonicPlane


def split_planes_list_by_type(planes_list):
    result = {
        'commercial_planes': [],
        'supersonic_planes': [],
        'commercial_ready_planes': [],
        'supersonic_ready_planes': [],
        'jet_planes': [],
        'jet_ready_planes': [],
    }
    for i in planes_list:
        if isinstance(i, SupersonicPlane):
            result['supersonic_planes'].append(i)
        if isinstance(i, CommercialPlane):
            result['commercial_planes'].append(i)
        if isinstance(i, JetPlane):
            result['jet_planes'].append(i)
        if isinstance(i, ReadySupersonicPlane):
            result['supersonic_ready_planes'].append(i)
        if isinstance(i, ReadyCommercialPlane):
            result['commercial_ready_planes'].append(i)
        if isinstance(i, ReadyJetPlane):
            result['jet_ready_planes'].append(i)
    return result
