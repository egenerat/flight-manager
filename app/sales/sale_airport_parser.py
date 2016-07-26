# coding=utf-8

import fm
from app.airport.airports_methods import switch_to_airport
from app.airport.airports_to_be_sold import build_airports_list, find_new_airports
from app.common.logger import logger
from app.common.constants import BANK_AIRPORT
from app.common.constants import PRICE_AIRPORT_AUTOMATIC_PURCHASE
from app.common.email_methods import notify
from app.common.http_methods import get_request
from app.common.http_methods import post_request
from app.common.string_methods import string_contains, format_amount
from app.common.target_urls import AIRPORT_SHOP_URL, BANK_WITHDRAW_URL, AIRPORT_BUY_URL, ALLIANCE_PAGE
from app.planes.concorde_to_be_sold import get_concorde_value_list, generate_email_string
from app.pm.pm_parser import __get_mp_nb, read_mp
from django.http import HttpResponse
from fm.databases.database_django import db_get_all_airports_sold, db_remove_all_airports_sold, db_insert_object
from fm.models import AirportsToBeSold


def sale_airports(request):
    result = ''
    fm.singleton_session.session = request.session
    page = get_request(AIRPORT_SHOP_URL)
    if not string_contains(u'Aucun aéroport en vente', page):
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
            if (i['price'] - i['cash']) < PRICE_AIRPORT_AUTOMATIC_PURCHASE:
                switch_to_airport(BANK_AIRPORT)
                # in case account < 0
                amount_to_withdraw = i['price'] * 1.04 + 10000000
                page = post_request(BANK_WITHDRAW_URL, {'cq': str(amount_to_withdraw)})
                # check if enough money
                page = get_request(AIRPORT_BUY_URL.format(airport_id=i['airport_id']))
                notify('FM : Bought one airport', page)
        if response:
            logger.error('Airport to be sold !')
            notify('FM : {} airport to be sold', 'Airport to be sold :\n{}'.format(airports_sold_nb, response))
            result += 'Airport for sale!\n'

    concorde_list = get_concorde_value_list()
    if len(concorde_list):
        tmp = generate_email_string(concorde_list)
        response = tmp['body']
        concorde_nb = tmp['title']
        notify('FM: {} Concorde for sale'.format(concorde_nb), response)
        result += 'concorde for sale'
    # page = get_request(SITE + '/compte.php?page=boutique1&affiche=9&c=4')
    #  if not string_contains(u'Aucune vente en cours', page):
    #      notify('FM : Tupolev for sale', 'Tupolev for sale')
    #      result += 'Tupolev for sale!\n'
    html_page = get_request(ALLIANCE_PAGE)
    if __get_mp_nb(html_page) > 0:
        response = read_mp()
        notify('FM: {} MPs'.format(response['mp_nb']), response['result'])
        result += ' mps'
    if not result:
        result = 'Nothing'
    return HttpResponse(result)
