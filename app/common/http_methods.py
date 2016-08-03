# -*- coding: iso-8859-15 -*-

import random
import re
import time

from app.common.logger import logger
from app.common.target_strings import LOGOUT_STRING_1
from app.common.target_strings import LOGOUT_STRING_2
from app.common.target_urls import LOGIN_PAGE
from app.common.target_urls import POST_LOGIN_PAGE
from lib import requests
from app.common import constants
from app.common.constants import USERNAME, PASSWORD, HEADER
from app.common.file_methods import read_login_file, save_to_file


def login():
    s = requests.session()
    s.get(LOGIN_PAGE, headers=HEADER)
    data = {"pseudo": USERNAME, "passe": PASSWORD}
    s.post(POST_LOGIN_PAGE, data, headers=HEADER)
    save_to_file(s)
    logger.warning('LOGIN')
    return s


def wait():
    time.sleep(0.3 + random.random()/2 )


def is_connected(page):
    p = re.compile(LOGOUT_STRING_1)
    p2 = re.compile(LOGOUT_STRING_2)
    return not len(p.findall(page)) and not len(p2.findall(page))


def __generic_request(method_name, address, post_data=None):
    s = read_login_file()
    if not s:
        logger.warning('file not found')
        s = login()
    result = getattr(s, method_name)(address, data=post_data, headers=constants.HEADER).text
    if not is_connected(result):
        logger.warning('not connected')
        s = login()
        try:
            result = getattr(s, method_name)(address, data=post_data, headers=constants.HEADER).text
        except:
            wait()
            result = getattr(s, method_name)(address, data=post_data, headers=constants.HEADER).text
    save_to_file(s)
    wait()
    return result


def get_request(address):
    return __generic_request('get', address)


def post_request(address, data):
    return __generic_request('post', address, data)
