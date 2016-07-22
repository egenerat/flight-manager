from app.common.constants import MAX_KM, KEROSENE_PRICE


# do not add dependency to CommercialPlane here, otherwise cyclic dependency


def get_plane_value(new_plane_value, km, kerosene_qty):
    value = (MAX_KM - km) / float(MAX_KM) * new_plane_value
    value += kerosene_qty * KEROSENE_PRICE
    return int(value)
