# coding=utf-8

import fm
from app.airport.airports_methods import money_before_taxes
from django.http import HttpResponse
from google.appengine.api import taskqueue


def view_taxes():
    money_before_taxes()
