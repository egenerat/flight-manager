# -*- coding: utf-8 -*-
import unittest

from app.common.http_methods_unittests import get_request
from app.common.string_methods import string_contains, get_values_from_regex
from app.common.target_parse_strings import PLANE_PANEL_AVAILABLE_HTML, ALLIANCE_CONCORDE_PATTERN_HTML
from app.common.target_urls import ALLIANCE_PAGE, ALLIANCE_PLANE_PANEL_URL, ALLIANCE_TAKE_PLANE_URL


class TestAirportParser(unittest.TestCase):

    def test_amount_needed(self):
        take_plane_from_alliance()
        # self.assertEqual(43900000, 0)


from mockito import when, mock, unstub

import requests
response = mock({'status_code': 200, 'text': 'Ok'})
when(requests).get('http://google.com/').thenReturn(response)

# use it
truc = requests.get('http://google.com/')
print(truc.text)

# clean up
unstub()


@unittest.skip("Not ready yet")
def take_plane_from_alliance(required_plane_type=10):
    page = get_request(ALLIANCE_PAGE)
    if string_contains(PLANE_PANEL_AVAILABLE_HTML.format(plane_type=required_plane_type), page):
        page = get_request(ALLIANCE_PLANE_PANEL_URL.format(plane_type=required_plane_type))
        plane_id = get_values_from_regex(ALLIANCE_CONCORDE_PATTERN_HTML, page)[0]
        page = get_request(ALLIANCE_TAKE_PLANE_URL.format(plane_id=plane_id))
        if u"Vous avez retiré avec succès l'avion" in page:
            return True
    return False


if __name__ == '__main__':
    unittest.main()
