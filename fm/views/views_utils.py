# -*- coding: utf-8 -*-
from google.appengine.api import taskqueue


def purge_queue():
    q = taskqueue.Queue('default')
    q.purge()






