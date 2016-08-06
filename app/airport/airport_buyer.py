# coding=utf-8
from app.airport.airports_methods import withdraw_from_alliance
from app.common.http_methods import get_request, post_request
from app.common.string_methods import exception_if_not_contains, get_values_from_regex, string_contains
from app.common.target_parse_strings import CONCORDE_PANEL_AVAILABLE_HTML, ALLIANCE_CONCORDE_PATTERN_HTML
from app.common.target_strings import SHOP_SUCCESSFUL_KEROSENE, SHOP_SUCCESSFUL_ENGINES, SHOP_SUCCESSFUL_PLANES
from app.common.target_urls import ALLIANCE_TAKE_CONCORDE_URL, ALLIANCE_PAGE, ALLIANCE_CONCORDE_PANEL_URL, \
    SHOP_ENGINE_4_URL, SHOP_ENGINE_5_URL, SHOP_ENGINE_6_URL, SHOP_KEROSENE_URL, SHOP_BUY_KEROSENE_URL
from app.planes.SupersonicPlane import SupersonicPlane


def buy_kerosene(litres):
    page = get_request(SHOP_KEROSENE_URL)
    # TODO check if there is kerosene available
    page = post_request(SHOP_BUY_KEROSENE_URL, {'cq': str(litres)})
    exception_if_not_contains(SHOP_SUCCESSFUL_KEROSENE, page, 'Error : could not buy kerosene')


def buy_engines(engines_nb, engine_type):
    url = {
        '4': SHOP_ENGINE_4_URL,
        '5': SHOP_ENGINE_5_URL,
        '6': SHOP_ENGINE_6_URL,
    }[engine_type]
    page = post_request(url, {'cq': str(engines_nb)})
    exception_if_not_contains(SHOP_SUCCESSFUL_ENGINES, page, 'Could not buy engines')


# TODO merge with fix_missing_planes
def buy_missing_planes(plane_class, missing_units):
    # if amount_needed(missing_planes) < self.airport.money:
    #     for aircraft_type, missing_units in missing_planes.iteritems():
    for _ in range(missing_units):
        if plane_class == SupersonicPlane:
            if take_concorde_from_alliance():
                return
        page = get_request(plane_class.buy_url)
        try:
            exception_if_not_contains(SHOP_SUCCESSFUL_PLANES, page, 'Could not buy a plane')
        except:
            withdraw_from_alliance(plane_class.price)
            # TODO be careful, the account may be < 0 before starting
            exception_if_not_contains(SHOP_SUCCESSFUL_PLANES, page, 'Could not buy a plane')


# TODO adapt all planes
def take_concorde_from_alliance():
    page = get_request(ALLIANCE_PAGE)
    if string_contains(CONCORDE_PANEL_AVAILABLE_HTML, page):
        page = get_request(ALLIANCE_CONCORDE_PANEL_URL)
        concorde_id = get_values_from_regex(ALLIANCE_CONCORDE_PATTERN_HTML, page)[0]
        page = get_request(ALLIANCE_TAKE_CONCORDE_URL.format(concorde_id=concorde_id))
        # Todo check if successful
        return True
    else:
        return False
