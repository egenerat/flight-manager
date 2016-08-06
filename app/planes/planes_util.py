# coding=utf-8

from app.common.constants import MAX_KM, KEROSENE_PRICE


# do not add dependency to CommercialPlane here, otherwise cyclic dependency
from app.common.target_parse_strings import SUPERSONICS_MODELS_HTML, COMMERCIAL_MODELS_HTML, JETS_MODELS_HTML


def get_plane_value(new_plane_value, km, kerosene_qty):
    value = (MAX_KM - km) / float(MAX_KM) * new_plane_value
    value += kerosene_qty * KEROSENE_PRICE
    return int(value)


def is_supersonic(string_model):
    return string_model in SUPERSONICS_MODELS_HTML


def is_jet(string_model):
    return string_model in JETS_MODELS_HTML


def is_regular_plane(string_model):
    return string_model in COMMERCIAL_MODELS_HTML
