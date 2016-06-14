import traceback

import fm
from app.common import logger
from app.common.email_methods import notify
from django.http import HttpResponse
from fm.bot_player import send_planes
from fm.views2 import purge_queue


def launch_missions(request):
    fm.singleton_session.session = request.session
    try:
        send_planes()
        logger.info('Successful')
    except Exception as e:
        exception_text = traceback.format_exc()
        logger.error(exception_text)
        notify('AS : There was a bug during execution', 'There was a bug during execution :\n'+str(exception_text))
#         taskqueue.add(url='/fm/launch_missions', countdown=60*30)
    return HttpResponse('started')


def start_launch_missions(request, taskqueue=None):
    purge_queue()
    taskqueue.add(url='/fm/launch_missions')
    return HttpResponse('Started: launch missions')


def start(request, taskqueue=None):
    taskqueue.add(url='/fm/refresh')
    return HttpResponse('Started')


def refresh(request):
    fm.singleton_session.session = request.session
    update_missions()
    return HttpResponse('Refresh done')

