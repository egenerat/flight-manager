from app.common.http_methods import post_request
from app.common.target_urls import SITE, HIRE_FLIGHT_ATTENDANTS_URL, HIRE_PILOTS_URL


def hire_pilotes(pilotes_nb):
    post_request(HIRE_PILOTS_URL, {'cq': pilotes_nb})


def hire_flight_attendants(flight_attendants_nb):
    post_request(HIRE_FLIGHT_ATTENDANTS_URL, {'cq': flight_attendants_nb})
