# -*- coding: utf-8 -*-

from app.planes.commercial_plane import CommercialPlane
from app.planes.jet_plane import JetPlane
from app.planes.supersonic_plane import SupersonicPlane


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
            if i.ready and i.is_usable:
                result['supersonic_ready_planes'].append(i)
        if isinstance(i, CommercialPlane):
            result['commercial_planes'].append(i)
            if i.ready and i.is_usable:
                result['commercial_ready_planes'].append(i)
        if isinstance(i, JetPlane):
            result['jet_planes'].append(i)
            if i.ready and i.is_usable:
                result['jet_ready_planes'].append(i)
    return result


def get_planes_nb_from_sorted_dict(planes_dict):
    return len(planes_dict['supersonic_planes'] + planes_dict['commercial_planes'] + planes_dict['jet_planes'])
