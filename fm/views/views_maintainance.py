import fm
from django.http import HttpResponse
from fm.fill_kero import fill_all_airports

# TODO cleanup and activate these views


def fill_kero(request):
    # only from market
    fm.singleton_session.session = request.session
    fill_all_airports()
    return HttpResponse('Done')


def start_fill_kero(request, taskqueue=None):
    taskqueue.add(url='/fm/fill_kero')
    return HttpResponse('Start fill kerozene')
