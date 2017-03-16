# -*- coding: utf-8 -*-

import random
import re
import time
from HTMLParser import HTMLParser

from app.common.logger import logger
from app.common.session_manager import get_session, save_session_in_cache
from app.common.target_strings import LOGOUT_STRING_1
from app.common.target_strings import LOGOUT_STRING_2
from app.common.target_urls import LOGIN_PAGE
from app.common.target_urls import POST_LOGIN_PAGE
from fm.databases.database_django import save_session_to_db
from lib import requests
from app.common.constants import USERNAME, PASSWORD, HEADER

parser = HTMLParser()


def authenticate_with_server():
    http_session = requests.session()
    http_session.get(LOGIN_PAGE, headers=HEADER)
    data = {"pseudo": USERNAME, "passe": PASSWORD, "souvenir": 1}
    http_session.post(POST_LOGIN_PAGE, data, headers=HEADER)
    logger.warning('LOGIN')
    save_session_in_cache(http_session)
    save_session_to_db()
    return http_session


def wait():
    time.sleep(0.3 + random.random() / 2)


def is_connected(page):
    p = re.compile(LOGOUT_STRING_1)
    p2 = re.compile(LOGOUT_STRING_2)
    return not len(p.findall(page)) and not len(p2.findall(page))


def __generic_request(method_name, address, post_data=None):
    http_session = get_session()
    if not http_session:
        logger.warning('No previous session found')
        http_session = authenticate_with_server()
    response = getattr(http_session, method_name)(address, data=post_data, headers=HEADER)
    response.encoding = 'utf-8'
    html_page = response.text
    if not is_connected(html_page):
        logger.warning('Session expired')
        http_session = authenticate_with_server()
        try:
            response = getattr(http_session, method_name)(address, data=post_data, headers=HEADER)
        except:
            wait()
            response = getattr(http_session, method_name)(address, data=post_data, headers=HEADER)
    response.encoding = 'utf-8'
    html_page = response.text
    html_page = parser.unescape(html_page)
    save_session_in_cache(http_session)
    wait()
    return html_page


def get_request(address):
    return __generic_request('get', address)


def post_request(address, data):
    return __generic_request('post', address, data)
