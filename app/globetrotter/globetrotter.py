from app.common.http_methods import get_request
from app.common.string_methods import get_values_from_regex
from app.common.target_urls import MOVE_AIRPORT_URL


def list_home_countries():
    page = get_request(MOVE_AIRPORT_URL)
    list_id = get_values_from_regex('"(\d+)"', page)
    return len(list_id)


def switch_to_country():
    pass


def download_all_missions():
    home_id = list_home_countries()
    for i in home_id:
        pass