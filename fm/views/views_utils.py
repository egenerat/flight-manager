# coding=utf-8
import traceback

from google.appengine.api import taskqueue

import fm
from app.common.email_methods import notify
from app.common.file_methods import read_saved_session_from_db, force_save_session_to_db
from app.common.logger import logger
from django.http import HttpResponse
# noinspection PyUnresolvedReferences
from fm.views.views_missions import view_launch_missions, view_parse_missions
# noinspection PyUnresolvedReferences
from fm.views.views_finances import view_taxes
# noinspection PyUnresolvedReferences
from fm.views.views_watcher import view_watcher

# (r'^test$', views_test.view_test),

# not ready
# (r'^fill_kero$', 'fill_kero'),
# (r'^engines$', 'engines'),
# (r'^quizz$', 'quizz'),
# (r'^answer$', 'answer'),
# (r'^missions$', 'represent_data'),
# (r'^refresh$', 'refresh'),
# (r'^stop$', 'stop'),


def purge_queue():
    q = taskqueue.Queue('default')
    q.purge()
    return q


''' First parameter request is not used. Replaced by _ for sonar '''
def view_generic_async_start(_, view_name):
    queue = purge_queue()
    action_url = '/fm/{}'.format(view_name)
    queue.add(url=action_url)
    return HttpResponse('Started: {}'.format(action_url))


''' First parameter request is not used. Replaced by _ for sonar '''
def view_generic(_, view_name):
    requested_view = 'view_{}()'.format(view_name)
    action_url = 'Requested view: {}'.format(requested_view)
    fm.singleton_session.session = read_saved_session_from_db()
    try:
        logger.info(action_url)
        eval(requested_view)
        logger.info('Successful')
    except Exception as e:
        exception_text = traceback.format_exc()
        logger.error(exception_text)
        notify('FM: Exception', 'Exception:\n{}'.format(exception_text))
        raise e
    finally:
        force_save_session_to_db()
    return HttpResponse('started')
