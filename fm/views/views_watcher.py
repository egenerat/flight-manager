# coding=utf-8

from app.sales.sale_airport_parser import sale_airports


def view_watcher(request):
    return sale_airports(request)
