from fm.models import Mission, AirportsToBeSold


def db_remove_all_missions():
    Mission.objects.all().delete()


def db_get_all_missions():
    return Mission.objects.all()


def db_get_all_airports_sold():
    return AirportsToBeSold.objects.all()


def db_remove_all_airports_sold():
    AirportsToBeSold.objects.all().delete()


def db_insert_object(obj):
    obj.save()


def db_count_missions():
    return Mission.objects.count()


def db_get_ordered_missions(origin_country, speed, capacity, nb_returned_missions, criteria):
    # Todo should read origin_country
    results = []
    missions = Mission.objects.all().filter(reputation_per_hour__gte=0).order_by(criteria)
    for i in missions:
        if i.km_nb <= speed and i.travellers_nb <= capacity:
            results.append(i)
    return results[:nb_returned_missions]
