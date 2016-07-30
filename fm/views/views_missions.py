# coding=utf-8

import traceback

import fm
from app.common.email_methods import notify
from app.common.file_methods import force_save_session_to_db, read_saved_session_from_db
from app.common.logger import logger
from app.manager.multi_airport_bot import MultiAirportBot
from django.http import HttpResponse
from fm.mission_handler import parse_all_missions


def view_launch_missions(request):
    fm.singleton_session.session = read_saved_session_from_db()
    try:
        bot = MultiAirportBot()
        bot.start()
        logger.info('Successful')
    except Exception as e:
        exception_text = traceback.format_exc()
        logger.error(exception_text)
        notify('FM : There was a bug during execution', 'There was a bug during execution :\n{}'.format(exception_text))
        raise e
    finally:
        force_save_session_to_db()
    return HttpResponse('started')


def view_parse_missions(request):
    parse_all_missions()
    return HttpResponse('Mission parsed')
