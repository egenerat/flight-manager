# coding=utf-8

class Staff(object):
    def __init__(self, **kwargs):
        mandatory_fields = ('ready_pilots', 'ready_flight_attendants')
        for field in mandatory_fields:
            setattr(self, field, kwargs.pop(field))
