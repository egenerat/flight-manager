# coding=utf-8

from app.manager.multi_airport_bot import MultiAirportBot
from django.http import HttpResponse
from fm.mission_handler import parse_all_missions, empty_db_missions
from fm.views.views_watcher import view_watcher


def view_launch_missions():
    bot = MultiAirportBot()
    bot.start()
    # plugged the view here
    view_watcher()


def view_parse_missions():
    parse_all_missions()


def view_empty_db_missions(_):
    empty_db_missions()
    return HttpResponse('emptied DB')
