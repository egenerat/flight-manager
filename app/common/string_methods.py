# coding=utf-8

import datetime
import re

from app.common.exceptions.string_not_found import StringNotFoundException
from app.common.target_parse_strings import AMOUNT_REGEX


def format_amount(amount):
    result = amount / 1000000
    return '{}M'.format(result)


def everything_between(text, begin, end):
    # idx1=text.find(begin)
    idx1 = [(m.start(0)) for m in re.finditer(begin, text)][0]
    if idx1 == -1:
        raise Exception
    idx2 = text.find(end, idx1)
    return text[idx1 + len(begin):idx2].strip()


#     regex = begin+'(.+)'+end
#     result = get_value_from_regex(regex, text)
#     return result.strip()

# def strip_special_characters_in_pattern(pattern):
    # return pattern.replace('?', '\?').replace('.', '\.')

def get_numeric_values_regex(regex, string):
    return [int(s) for s in re.findall(regex, string)[0]]


def get_values_from_regex(regex, string):
    return re.findall(regex, string)


def get_value_from_regex(regex, string):
    try:
        result = get_values_from_regex(regex, string)[0]
    except:
        message = 'String not found: regex: {} in string: {}'.format(regex.encode('utf-8'), string.encode('utf-8'))
        raise StringNotFoundException(message)
    return result


def get_int_from_regex(regex, string):
    return int(get_value_from_regex(regex, string))


def get_amount(string):
    return get_amount_from_regex(AMOUNT_REGEX, string)


# direct call deprecated
def get_amount_from_regex(regex, string):
    return int(''.join(get_value_from_regex(regex, string)))


def date_from_regex_result(a_tuple):
    return datetime.datetime(int(a_tuple[2]), int(a_tuple[1]), int(a_tuple[0]), int(a_tuple[3]), int(a_tuple[4]))


def string_contains(regex, string):
    return len(get_values_from_regex(regex, string))


def exception_if_not_contains(regex, string, message=''):
    if not string_contains(regex, string):
        raise Exception('Regex error : string not found. ' + message)
