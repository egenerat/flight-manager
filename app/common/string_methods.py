# -*- coding: iso-8859-15 -*-

import datetime
import re
from app.common.logger import logger

MULTI_SPACE = '[\S+\n\r\s]+'


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
    result = None
    try:
        result = get_values_from_regex(regex, string)[0]
    except:
        logger.error('String not found: regex: ' + regex + ' in string: ' + string)
        raise Exception('String not found: regex: ' + regex + ' in string: ' + string)
    return result


def get_int_from_regex(regex, string):
    return int(get_value_from_regex(regex, string))


def get_amount(string):
    return get_amount_from_regex(u'(-?)(?:(\d+),)?(?:(\d+),)?(?:(\d+),)?(\d+)', string)


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


def string_methods_test():
    string = "-10,198,127 $"
    is_valid = get_amount(string) == -10198127
    return '{}: {}\n'.format(string, is_valid)

