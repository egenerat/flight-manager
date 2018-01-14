# -*- coding: utf-8 -*-


class Airport(object):
    def __init__(self, **kwargs):
        mandatory_fields = ('country', 'money', 'kerosene_supply', 'kerosene_capacity', 'engines_supply',
                            'planes_capacity', 'staff', 'airport_name')
        for field in mandatory_fields:
            setattr(self, field, kwargs.pop(field))
            # TODO Move the list of planes as a property of the airport

    def __str__(self):
        return 'Airport {} H{} {}'.format(self.airport_name.encode('utf-8'), self.planes_capacity, self.country.encode('utf-8'))
