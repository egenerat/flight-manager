# -*- coding: utf-8 -*-


class Airport(object):

    def __init__(self, **kwargs):
        mandatory_fields = ('country', 'money', 'kerozene_supply', 'kerozene_capacity', 'engines_supply',
                             'planes_capacity', 'staff', 'airport_name')
        for field in mandatory_fields:
            setattr(self, field, kwargs.pop(field))
