import traceback

import fm
from app.common import logger
from app.common.email_methods import notify
from app.manager.multi_airport_bot import MultiAirportBot
from django.http import HttpResponse
from fm.mission_handler import parse_all_missions
from fm.views.views_utils import purge_queue

# TODO deprecated file


def launch_missions(request):
    fm.singleton_session.session = request.session
    try:
        bot = MultiAirportBot()
        bot.start()()
        logger.info('Successful')
    except Exception as e:
        exception_text = traceback.format_exc()
        logger.error(exception_text)
        notify('AS : There was a bug during execution', 'There was a bug during execution :\n{}'.format(exception_text))
    return HttpResponse('started')


def start_launch_missions(request, taskqueue=None):
    fm.singleton_session.session = request.session
    purge_queue()
    taskqueue.add(url='/fm/launch_missions')
    return HttpResponse('Started: launch missions')


def start_parse_missions(request, taskqueue=None):
    fm.singleton_session.session = request.session
    taskqueue.add(url='/fm/refresh')
    return HttpResponse('Started')


def parse_missions(request):
    parse_all_missions()
    return HttpResponse('Mission parsed')

