# coding=utf-8

from app.manager.multi_airport_bot import MultiAirportBot
from fm.mission_handler import parse_all_missions, empty_db_missions


def view_launch_missions():
    bot = MultiAirportBot()
    bot.start()


def view_parse_missions():
    parse_all_missions()


def view_empty_db_missions():
    empty_db_missions()
