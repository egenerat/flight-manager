# coding=utf-8

from app.common.http_methods import post_request
from app.common.target_urls import HIRE_FLIGHT_ATTENDANTS_URL, HIRE_PILOTS_URL, HIRE_MECHANICS_URL


def hire_pilots(pilots_nb):
    post_request(HIRE_PILOTS_URL, {'cq': pilots_nb})


def hire_flight_attendants(flight_attendants_nb):
    post_request(HIRE_FLIGHT_ATTENDANTS_URL, {'cq': flight_attendants_nb})


def hire_mechanics(mechanics_nb):
    post_request(HIRE_MECHANICS_URL, {'cq': mechanics_nb})
