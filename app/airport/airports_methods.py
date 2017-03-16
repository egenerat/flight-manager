# -*- coding: utf-8 -*-
from app.common.constants import EXCLUDE_LIST
from app.common.http_methods import get_request, post_request
from app.common.string_methods import get_amount_from_regex, \
    exception_if_not_contains, get_values_from_regex
from app.common.target_parse_strings import AIRPORT_CASH_REGEX, ALLIANCE_CASH_REGEX, AIRPORTS_ID_REGEX
from app.common.target_strings import BANK_DEPOSIT_SUCCESSFUL, ALLIANCE_DEPOSIT_SUCCESSFUL
from app.common.target_urls import AIRPORT_MENU_PAGE, BANK_PAGE, ALLIANCE_PAGE, SWITCH_TO_AIRPORT_URL, \
    ALLIANCE_WITHDRAW_CASH_URL, ALLIANCE_DEPOSIT_CASH_URL, BANK_DEPOSIT_URL


def get_other_airports_id():
    page = get_request(AIRPORT_MENU_PAGE)
    other_airports = get_values_from_regex(AIRPORTS_ID_REGEX, page)
    return other_airports


def filter_airports(airports_list):
    return [airport for airport in airports_list if airport not in EXCLUDE_LIST]


def switch_to_airport(airport_id):
    get_request(AIRPORT_MENU_PAGE)
    post_request(SWITCH_TO_AIRPORT_URL, {'id_aeroport': airport_id})


def move_money_to_bank(amount=None):
    if not amount:
        page = get_request(BANK_PAGE)
        amount = get_amount_from_regex(AIRPORT_CASH_REGEX, page)
    else:
        get_request(BANK_PAGE)
    result = post_request(BANK_DEPOSIT_URL, {'cq': amount})
    exception_if_not_contains(BANK_DEPOSIT_SUCCESSFUL, result)


def move_money_to_alliance(amount=None):
    if not amount:
        page = get_request(ALLIANCE_PAGE)
        amount = get_amount_from_regex(AIRPORT_CASH_REGEX, page)
    if amount > 0:
        result = post_request(ALLIANCE_DEPOSIT_CASH_URL, {'cq': amount})
        exception_if_not_contains(ALLIANCE_DEPOSIT_SUCCESSFUL, result)


def withdraw_from_alliance(amount=None):
    if not amount:
        page = get_request(ALLIANCE_PAGE)
        # TODO Put all the amounts regex in a constant
        amount = get_amount_from_regex(ALLIANCE_CASH_REGEX, page)
    post_request(ALLIANCE_WITHDRAW_CASH_URL, {'cq': amount})


def money_before_taxes():
    airports_list = get_other_airports_id()
    # Todo buy kerosene and/or engines at this point
    for i in airports_list:
        switch_to_airport(i)
        move_money_to_alliance()
        # switch_to_airport(BANK_AIRPORT)
        # withdraw_from_alliance()
        # move_money_to_bank()
