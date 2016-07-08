from abc import ABCMeta


class RootPlane(object):

    def __init__(self, **kwargs):
        __metaclass__ = ABCMeta
        mandatory_fields = ('plane_id', 'ready')
        for field in mandatory_fields:
            setattr(self, field, kwargs.pop(field))
        self.required_maintenance = kwargs.pop('required_maintenance', False)
