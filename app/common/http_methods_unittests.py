# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser

from lib import requests

parser = HTMLParser()


def get_request(address):
    response = requests.get(address)
    response.encoding = 'utf-8'
    html_page = response.text
    html_page = parser.unescape(html_page)
    return html_page
