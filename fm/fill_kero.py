# -*- coding: utf-8 -*-

import re

from app.airport.Airport import Airport
from app.airport.airports_methods import get_other_airports_id, switch_to_airport, withdraw_from_alliance
from app.common.http_methods import get_request, post_request
from app.common.string_methods import get_amount, exception_if_not_contains
from app.common.target_strings import SHOP_SUCCESSFUL_KEROSENE, SHOP_NO_SALE
from app.common.target_urls import SHOP_USED_KEROSENE_URL, QUICK_REFILL_URL, SHOP_BUY_USED_KEROSENE_URL


# todo refactor
def fill_all_airports():
    other_airports = get_other_airports_id()
    # switch on all airports
    for j in other_airports:
        switch_to_airport(j)
        current_airport = Airport()
        capacity = current_airport.get_kerosene_capacity()
        stock = current_airport.get_kerosene_supply()
        difference = capacity - stock

        if difference > 0:
            page = get_request()
            available_offers = extract_available_offers(page)
            # while difference > 0:
            # the list should be copied so that it's a copy that's altered
            if available_offers:
                current_offer = available_offers.pop()
                if difference < current_offer['quantity']:
                    try:
                        buy_market_kero(difference, current_offer['sell_id'])
                    except:
                        # plus quick refill
                        withdraw_from_alliance(int(current_offer['price'] * difference) + 2500)
                        buy_market_kero(difference, current_offer['sell_id'])
        quick_refill = get_request(QUICK_REFILL_URL)
        # exception_if_not_contains('Vous venez de mettre un total de')
        # exception_if_not_contains("aucun plein n'est possible")
        current_airport = Airport()
        capacity = current_airport.get_kerosene_capacity()
        stock = current_airport.get_kerosene_supply()
        difference = capacity - stock

        if difference > 0:
            page = get_request(SHOP_USED_KEROSENE_URL)
            available_offers = extract_available_offers(page)
            # while difference > 0:
            # the list should be copied so that it's a copy that's altered
            if available_offers:
                current_offer = available_offers.pop()
                if difference < current_offer['quantity']:
                    try:
                        buy_market_kero(difference, current_offer['sell_id'])
                    except:
                        # plus quick refill
                        withdraw_from_alliance(int(current_offer['price'] * difference) + 2500)
                        buy_market_kero(difference, current_offer['sell_id'])


def get_market_kero_page():
    return get_request('http://localhost/AS/marketplace_kerosene_2sellers.html')


def buy_market_kero(quantity, sale_id):
    body = {
        'cq': quantity,
        'mon_champ': sale_id
    }
    response = post_request(SHOP_BUY_USED_KEROSENE_URL, body)
    exception_if_not_contains(SHOP_SUCCESSFUL_KEROSENE, response)


def extract_available_offers(page):
    if not re.findall(SHOP_NO_SALE, page):
        result = re.findall(
            '<td class="Brocante1"><input type="radio" name="mon_champ" value="\d+"></td>[.\S+\n\r\s]*?</tr>', page)
        sell_list = []
        for i in result:
            sell_id = re.findall('<input type="radio" name="mon_champ" value="(\d+)">', i)[0]
            amount_html = re.findall('<td class="Brocante3">(.+)</td>', i)[0]
            quantity = get_amount(amount_html)
            price = float(re.findall('<td class="Brocante2">(\d+\.?\d*) \$</td>', i)[0])
            obj = {
                'sell_id': sell_id,
                'quantity': quantity,
                'price': price
            }
            sell_list.append(obj)
        sell_list = sorted(sell_list, key=lambda i: i['price'])
        return sell_list
