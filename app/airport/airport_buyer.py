# -*- coding: utf-8 -*-
from app.airport.airports_methods import withdraw_from_alliance
from app.common.http_methods import get_request, post_request
from app.common.string_methods import exception_if_not_contains, get_values_from_regex, string_contains
from app.common.target_parse_strings import PLANE_PANEL_AVAILABLE_HTML, ALLIANCE_CONCORDE_PATTERN_HTML
from app.common.target_strings import SHOP_SUCCESSFUL_PLANES, ALLIANCE_TAKE_PLANE_SUCCESSFUL
from app.common.target_urls import ALLIANCE_TAKE_PLANE_URL, ALLIANCE_PAGE, ALLIANCE_PLANE_PANEL_URL, \
    SHOP_ENGINE_4_URL, SHOP_ENGINE_5_URL, SHOP_ENGINE_6_URL, SHOP_KEROSENE_URL, SHOP_BUY_KEROSENE_URL, SHOP_GENERIC_URL


def buy_kerosene(litres):
    get_request(SHOP_KEROSENE_URL)
    # TODO check if there is kerosene available
    post_request(SHOP_BUY_KEROSENE_URL, {'cq': str(litres)})
    # exception_if_not_contains(SHOP_SUCCESSFUL_KEROSENE, page, 'Error : could not buy kerosene')


def buy_engines(engines_nb, engine_type):
    url = {
        '4': SHOP_ENGINE_4_URL,
        '5': SHOP_ENGINE_5_URL,
        '6': SHOP_ENGINE_6_URL,
    }[engine_type]
    post_request(url, {'cq': str(engines_nb)})
    # exception_if_not_contains(SHOP_SUCCESSFUL_ENGINES, page, 'Could not buy engines')


# TODO merge with fix_missing_planes
def buy_missing_planes(plane_class, missing_units):
    # if amount_needed(missing_planes) < self.airport.money:
    #     for aircraft_type, missing_units in missing_planes.iteritems():
    for _ in range(missing_units):
        plane_type_id = plane_class.shop_plane_type
        if take_plane_from_alliance(plane_type_id):
            return
        page = buy_plane_from_shop(plane_type_id)
        try:
            exception_if_not_contains(SHOP_SUCCESSFUL_PLANES, page, 'Could not buy a plane')
        except:
            withdraw_from_alliance(plane_class.price)
            # TODO be careful, the account may be < 0 before starting
            # exception_if_not_contains(SHOP_SUCCESSFUL_PLANES, page, 'Could not buy a plane')


def buy_plane_from_shop(plane_type_id):
    return get_request(SHOP_GENERIC_URL.format(plane_type_id=plane_type_id))


def take_plane_from_alliance(plane_type_id):
    page = get_request(ALLIANCE_PAGE)
    if string_contains(PLANE_PANEL_AVAILABLE_HTML.format(plane_type=plane_type_id), page):
        page = get_request(ALLIANCE_PLANE_PANEL_URL.format(plane_type=plane_type_id))
        planes_id = get_values_from_regex(ALLIANCE_CONCORDE_PATTERN_HTML, page)
        if len(planes_id):
            plane_id = planes_id[0]
            page = get_request(ALLIANCE_TAKE_PLANE_URL.format(plane_id=plane_id))
            if ALLIANCE_TAKE_PLANE_SUCCESSFUL in page:
                return True
    return False
