# coding=utf-8


class Staff(object):
    def __init__(self, **kwargs):
        mandatory_fields = ('total_pilots', 'ready_pilots', 'total_flight_attendants', 'ready_flight_attendants',
                            'total_mechanics')
        for field in mandatory_fields:
            setattr(self, field, kwargs.pop(field))
