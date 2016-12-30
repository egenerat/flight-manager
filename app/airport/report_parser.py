# -*- coding: iso-8859-1 -*-
from app.common.string_methods import everything_between, get_int_from_regex, get_amount_from_regex, get_amount, \
    get_value_from_regex
from app.common.target_parse_strings import AMOUNT_REGEX


def extract_daily_report(full_html_page):
    return everything_between(full_html_page, u"<u>Bilan de la journ&eacute;e</u> :<br /><br />", u"La variation se calcule sur la comparaison de la valeur")


def extract_crash_number(html_report):
    """html report is only the daily or weekly table"""
    string_amount = get_value_from_regex('<td class="bilan1"><font color="red">([^%]+?)</font></td>', html_report)
    return get_amount(string_amount)


def report_parser(full_html_page):
    daily_report = extract_daily_report(full_html_page)
    return {
        'daily': {
            'crashes': extract_crash_number(daily_report)
        }
    }
