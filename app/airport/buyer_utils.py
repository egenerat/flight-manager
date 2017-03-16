# -*- coding: utf-8 -*-

def amount_needed(missing_planes):
    amount = 0
    for aircraft_type, missing_units in missing_planes.iteritems():
        amount += missing_units * aircraft_type.price
    return amount