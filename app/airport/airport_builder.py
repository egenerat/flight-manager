import requests

from app.airport.Airport import Airport
from app.airport.Staff import Staff
from app.airport.airports_parsers import get_country, get_money, get_kerozene_supply, get_kerozene_capacity, \
    get_engines_supply, get_planes_capacity, get_airport_name
from app.airport.staff_parser import get_pilotes, get_flight_attendants
from app.common.target_urls import MY_AIRPORT, STAFF_PAGE_TEST


def build_airport(airport_html, staff_html):
    country = get_country(airport_html)
    money = get_money(airport_html)
    kerozene_supply = get_kerozene_supply(airport_html)
    kerozene_capacity = get_kerozene_capacity(airport_html)
    engines_supply = get_engines_supply(airport_html)
    planes_capacity = get_planes_capacity(airport_html)
    airport_name = get_airport_name(airport_html)
    staff = build_staff(staff_html)
    return Airport(country=country, money=money, kerozene_supply=kerozene_supply, kerozene_capacity=kerozene_capacity, engines_supply=engines_supply,
    planes_capacity=planes_capacity, airport_name=airport_name, staff=staff)


def build_staff(html_page):
    total_pilots, busy_pilots = get_pilotes(html_page)
    ready_pilots = total_pilots - busy_pilots
    total_flight_attendants, busy_flight_attendants = get_flight_attendants(html_page)
    ready_flight_attendants = total_flight_attendants - busy_flight_attendants
    return Staff(ready_pilots=ready_pilots, ready_flight_attendants=ready_flight_attendants)


if __name__ == '__main__':
    staff_page = requests.get(STAFF_PAGE_TEST).text
    airport_page = requests.get(MY_AIRPORT).text
    build_airport(airport_page, staff_page)
