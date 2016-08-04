# coding=utf-8

airport = None

session_to_server = None


def get_airport():
    return airport


def set_airport(current_airport):
    global airport
    airport = current_airport

# TODO: replace, otherwise deployed on the platform
local_mode = True
