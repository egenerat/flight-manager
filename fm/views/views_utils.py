# coding=utf-8

from google.appengine.api import taskqueue

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
