# coding=utf-8

import fm
from app.airport.airports_methods import money_before_taxes
from django.http import HttpResponse
from google.appengine.api import taskqueue


def taxes(request):
    fm.singleton_session.session = request.session
    money_before_taxes()
    return HttpResponse('Taxes ok!')


def start_taxes(request):
    taskqueue.add(url='/fm/taxes')
    return HttpResponse('Started: taxes')
