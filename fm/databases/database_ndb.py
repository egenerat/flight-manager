# coding=utf-8

from fm.models import Mission


def db_remove_all_missions():
    #     db_remove_all_missions()
    obj_list = Mission.query()
    for i in obj_list:
        i.key.delete()


def db_get_all_missions():
    #     Mission.objects.all()
    return Mission.query()


def db_insert_object(obj):
    #     obj.save()
    obj.put()


def db_count_missions():
    #     Mission.objects.count()
    len(db_get_all_missions())
    return 0


def db_get_ordered_missions(origin_country, speed, capacity):
    raise Exception('Mission not implemented')
    # return Mission.objects.all().filter(travellers_nb__lte=capacity).order_by('-revenue_per_hour')
