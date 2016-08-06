# coding=utf-8

import re

from app.common.http_methods import get_request
from app.common.string_methods import everything_between, get_int_from_regex, get_values_from_regex
from app.common.target_parse_strings import PM_NB_REGEX, PM_BOX_PM_IDS_REGEX, PM_BEGIN_MESSAGE_PATTERN, \
    PM_END_MESSAGE_PATTERN
from app.common.target_urls import PM_BOX_URL, PM_OPEN_URL
from django.utils.html import strip_tags


def __get_mp_nb(html_page):
    return get_int_from_regex(PM_NB_REGEX, html_page)


def get_pm_ids(pm_box_page):
    pm_ids = get_values_from_regex(PM_BOX_PM_IDS_REGEX, pm_box_page)
    return pm_ids

def read_mp():
    result = ''
    pm_box_page = get_request(PM_BOX_URL)
    pm_ids = get_pm_ids(pm_box_page)
    mp_nb = len(pm_ids)
    for pm_id in pm_ids:
        page = get_request(PM_OPEN_URL.format(pm_id=pm_id))
        begin = PM_BEGIN_MESSAGE_PATTERN
        end = PM_END_MESSAGE_PATTERN
        mp_content = everything_between(page, begin, end)
        mp_content = strip_tags(re.findall('(.[\S+\n\r\s]+)<br /><br /></td>', mp_content)[0])
        result += mp_content + '\n\n\n'
    return {
        'mp_nb': mp_nb,
        'result': result
    }
