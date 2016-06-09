from app.common.constants import MAX_KM, KEROZENE_PRICE


def get_plane_value(new_plane_value, km, kerozene_qty):
    value = (MAX_KM - km) / float(MAX_KM) * new_plane_value
    value += kerozene_qty * KEROZENE_PRICE
    return int(value)
