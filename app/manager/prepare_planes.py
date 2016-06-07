from app.airport.airport_buyer import buy_engines


def change_engines_if_needed(planes_list):
    planes_queue_commercial = []
    for i in planes_list:
        if i.engines_to_be_changed():
            planes_queue_commercial.append(i)
    # check if enough engines, otherwise buy
    engines_nb = len(planes_queue_commercial)
    buy_engines(engines_nb, '4')
    planes_list(planes_queue_commercial)
