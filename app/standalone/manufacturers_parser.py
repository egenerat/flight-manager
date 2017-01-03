# coding=utf-8
from app.common.http_methods import get_request


def parse_manufacturers():
    """Avions de ligne"""
    return [{

    }]


def parse_models():
    return [{

    }]


def parse_specifications():
    return [{

    }]


def passengers_capacity():
    pass


def pyquery(html_page):
    from pyquery import PyQuery as pq
    doc = pq(html_page)
    print(len(doc('p')))
    print(doc('p').text())


def get_manufacturers_page():
    html_page = get_request("http://172.17.0.1/test_pages/planes_shop_1st_page.html")
    result = parse_manufacturers(html_page)


def get_models_page():
    html_page = get_request("http://172.17.0.1/test_pages/planes_shop_2nd_page.html")
    result = parse_models(html_page)


def get_specifications_page():
    html_page = get_request("http://172.17.0.1/test_pages/planes_shop_3rf_page_details.html")
    result = parse_specifications(html_page)

