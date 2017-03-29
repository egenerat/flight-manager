# -*- coding: utf-8 -*-

from app.airport.Airport import Airport
from app.airport.Staff import Staff
from app.airport.airports_parsers import get_country, get_money, get_kerosene_supply, get_kerosene_capacity, \
    get_engines_supply, get_planes_capacity, get_airport_name
from app.airport.staff_parser import get_pilots, get_flight_attendants, get_mechanics


def build_airport_from_html(airport_html, staff_html):
    country = get_country(airport_html)
    money = get_money(airport_html)
    kerosene_supply = get_kerosene_supply(airport_html)
    kerosene_capacity = get_kerosene_capacity(airport_html)
    engines_supply = get_engines_supply(airport_html)
    planes_capacity = get_planes_capacity(airport_html)
    airport_name = get_airport_name(airport_html)
    staff = build_staff(staff_html)
    return Airport(country=country, money=money, kerosene_supply=kerosene_supply, kerosene_capacity=kerosene_capacity,
                   engines_supply=engines_supply, planes_capacity=planes_capacity,
                   airport_name=airport_name, staff=staff)


def build_staff(html_page):
    total_pilots, busy_pilots = get_pilots(html_page)
    ready_pilots = total_pilots - busy_pilots
    total_flight_attendants, busy_flight_attendants = get_flight_attendants(html_page)
    ready_flight_attendants = total_flight_attendants - busy_flight_attendants
    # TODO fill the correct value
    total_mechanics = get_mechanics(html_page)
    return Staff(total_pilots=total_pilots, total_flight_attendants=total_flight_attendants,
                 total_mechanics=total_mechanics, ready_pilots=ready_pilots,
                 ready_flight_attendants=ready_flight_attendants)
