# -*- coding: utf-8 -*-

from app.airport.airports_methods import switch_to_airport
from app.airport.sale_airports_parser import build_airports_list, find_new_airports
from app.common.logger import logger
from app.common.constants import BANK_AIRPORT
from app.common.constants import PRICE_AIRPORT_AUTOMATIC_PURCHASE
from app.common.email_methods import notify
from app.common.http_methods import get_request
from app.common.http_methods import post_request
from app.common.string_methods import string_contains, format_amount
from app.common.target_strings import SHOP_NO_AIRPORT_SALE
from app.common.target_urls import AIRPORT_SHOP_URL, BANK_WITHDRAW_URL, AIRPORT_BUY_URL, ALLIANCE_PAGE, \
    SHOP_USED_TUPOLEV_URL
from app.pm.pm_parser import __get_mp_nb, read_mp
from fm.databases.database import db_get_all_airports_sold, db_remove_all_airports_sold, db_insert_object
from fm.models import AirportsToBeSold


def get_sale_value_tupolev():
    page = get_request(SHOP_USED_TUPOLEV_URL)
    if not string_contains(u'Aucune vente en cours', page):
        notify('FM : Tupolev for sale', 'Tupolev for sale')


def get_mp():
    html_page = get_request(ALLIANCE_PAGE)
    if __get_mp_nb(html_page) > 0:
        response = read_mp()
        notify('FM: {} MPs'.format(response['mp_nb']), response['result'])


def get_sale_airports():
    page = get_request(AIRPORT_SHOP_URL)
    if not string_contains(SHOP_NO_AIRPORT_SALE, page):
        airports_list = build_airports_list(page)
        old_airports = db_get_all_airports_sold()
        new_airports = find_new_airports(old_airports, airports_list)
        db_remove_all_airports_sold()
        for i in airports_list:
            a_mission = AirportsToBeSold(**i)
            db_insert_object(a_mission)
        airports_sold_nb = len(new_airports)
        response = ''
        for i in new_airports:
            response += 'H{} :  {} $, cash: {}\n'.format(i['capacity'], i['price'], format_amount(i['cash']))
            # TODO improve buying policy
            if (i['price'] - i['cash']) < PRICE_AIRPORT_AUTOMATIC_PURCHASE and i[
                'price'] < 20000000000:  # and i['price'] > 0:
                switch_to_airport(BANK_AIRPORT)
                # in case account < 0
                amount_to_withdraw = i['price'] * 1.04 + 50000000
                page = post_request(BANK_WITHDRAW_URL, {'cq': str(amount_to_withdraw)})
                # check if enough money (in case account was < 0 before)
                page = get_request(AIRPORT_BUY_URL.format(airport_id=i['airport_id']))
                notify('FM : Bought one airport', page)
        if response:
            logger.info('Airport to be sold !')
            notify('FM : {} airport to be sold', 'Airport to be sold :\n{}'.format(airports_sold_nb, response))
