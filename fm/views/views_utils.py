# coding=utf-8
import traceback

from google.appengine.api import taskqueue

import fm
from app.common.email_methods import notify
from app.common.file_methods import read_saved_session_from_db, force_save_session_to_db
from app.common.logger import logger
from django.http import HttpResponse


def purge_queue():
    q = taskqueue.Queue('default')
    q.purge()
    return q

def view_generic_async_start(request, view_name):
    queue = purge_queue()
    action_url = '/fm/{}'.format(view_name)
    queue.add(url=action_url)
    return HttpResponse('Started: {}'.format(action_url))


def view_decorator(function):
    def wrapper():
        fm.singleton_session.session = read_saved_session_from_db()
        try:
            function()
            logger.info('Successful')
        except Exception as e:
            exception_text = traceback.format_exc()
            logger.error(exception_text)
            notify('FM: Exception', 'Exception:\n{}'.format(exception_text))
            raise e
        finally:
            force_save_session_to_db()
        return HttpResponse('started')
    return wrapper