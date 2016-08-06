# coding=utf-8

from app.common.string_methods import get_value_from_regex, everything_between, \
    string_contains, get_amount_from_regex
from app.common.target_parse_strings import PLANE_MODEL_REGEX, PLANE_ID_REGEX, PLANE_STATUS_REGEX, PLANE_KEROSENE_REGEX, \
    PLANE_KM_REGEX, PLANE_ENGINES_HOURS_REGEX, END_PLANES_TABLE_HTML, BEGIN_PLANES_TABLE_HTML
from app.common.target_strings import PLANE_MAINTAINANCE_ONGOING, PLANE_IN_SALE, PLANE_MAINTENANCE_NEEDED, \
    PLANE_OVER_500K
from app.planes.planes_factory import usable_planes_factory, planes_factory


def __get_model(html_line):
    return get_value_from_regex(PLANE_MODEL_REGEX, html_line)


def __get_planes_panel(html):
    return everything_between(html, BEGIN_PLANES_TABLE_HTML, END_PLANES_TABLE_HTML)


def build_plane_from_line(html_line):
    required_maintenance = False
    endlife = False
    plane_model = __get_model(html_line)
    plane_id = get_value_from_regex(PLANE_ID_REGEX, html_line)
    ready = True

    if string_contains(PLANE_IN_SALE, html_line) or string_contains(PLANE_MAINTAINANCE_ONGOING, html_line):
        ready = False
    elif string_contains(PLANE_OVER_500K, html_line):
        ready = False
        endlife = True
    elif string_contains(PLANE_MAINTENANCE_NEEDED, html_line):
        ready = False
        required_maintenance = True
    if not ready:
        return planes_factory(plane_model)(plane_id=plane_id, ready=ready, required_maintenance=required_maintenance,
                                           endlife=endlife)
    else:
        status = get_value_from_regex(PLANE_STATUS_REGEX, html_line)
        ready = True if status == 'I' else False
        kerosene = get_amount_from_regex(PLANE_KEROSENE_REGEX, html_line)
        hours = get_value_from_regex(PLANE_ENGINES_HOURS_REGEX, html_line)
        km_nb = get_amount_from_regex(PLANE_KM_REGEX, html_line)
        current_engine_hours = hours[0]
        maximum_engine_hours = hours[1]
        return usable_planes_factory(plane_model)(plane_id=plane_id, ready=ready,
                                                  required_maintenance=required_maintenance,
                                                  status=status, kerosene=kerosene,
                                                  current_engine_hours=current_engine_hours, km=km_nb,
                                                  maximum_engine_hours=maximum_engine_hours)


def build_planes_from_html(html):
    result = []
    html = __get_planes_panel(html)
    lines = html.split('<tr>')[2:]
    for a_line in lines:
        a_plane = build_plane_from_line(a_line)
        if a_plane:
            result.append(a_plane)
    return result
