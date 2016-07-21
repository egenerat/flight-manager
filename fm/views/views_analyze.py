import fm
from django.shortcuts import render_to_response

from app.airport.Airport import Airport
from app.airport.airports_methods import get_other_airports_id
from app.airport.airports_methods import switch_to_airport
from app.common.constants import CONCORDE_CAPACITY, CONCORDE_SPEED
from app.common.http_methods import get_request
from app.common.string_methods import format_amount
from app.common.target_urls import PLANES_PAGE
from app.parsers.planesparser import build_planes_from_html
from django.http import HttpResponse
from fm.databases.database_django import db_get_ordered_missions, db_get_ordered_missions_multi_type, \
    planes_needed_by_category


def view_top_missions(request):
    mission_list = db_get_ordered_missions_multi_type(200, '-reputation_per_hour')
    nb_planes_needed = planes_needed_by_category(mission_list)
    return render_to_response('list_missions.html', {'missions': mission_list, 'planes_needed': nb_planes_needed})


def represent_data(request):
    country_list = ['France', 'Italie', 'Suisse', 'Turquie']
    result = {}
    missions_list = []
    for i in country_list:
        missions_list = db_get_ordered_missions(i, CONCORDE_CAPACITY, CONCORDE_SPEED, 84, '-reputation_per_hour')
        total_reputation_36 = 0
        total_revenue_36 = 0
        total_reputation_54 = 0
        total_revenue_54 = 0
        total_reputation_84 = 0
        total_revenue_84 = 0
        for idx,a_mission in enumerate(missions_list):
            total_revenue_84 += a_mission.revenue_per_hour
            total_reputation_84 += a_mission.reputation_per_hour
            if idx < 54:
                total_revenue_54 += a_mission.revenue_per_hour
                total_reputation_54 += a_mission.reputation_per_hour
            if idx < 36:
                total_revenue_36 += a_mission.revenue_per_hour
                total_reputation_36 += a_mission.reputation_per_hour
        result[i] = {
            'total_reputation_84':total_reputation_84/84,
            'total_revenue_84':total_revenue_84/84,
            'total_reputation_54':total_reputation_54/54,
            'total_revenue_54':total_revenue_54/54,
            'total_reputation_36':total_reputation_36/36,
            'total_revenue_36':total_revenue_36/36,
        }
    return render_to_response('missions.html',{'result':result, 'missions':missions_list})


def planes_value(request):
    response = ''
    fm.singleton_session.session = request.session
    other_airports = get_other_airports_id()
    for j in other_airports:
        sum = 0
        planes_nb = 0
        switch_to_airport(j)
        current_airport = Airport()
        page = get_request(PLANES_PAGE)
        ready_planes = build_planes_from_html(page, True)
        for i in ready_planes:
            if i.get_value:
                if i.get_value():
                    sum += i.get_value()
                    planes_nb += 1
        response += '{}({}/{}) <br/><br/>'.format(current_airport.get_airport_name(), planes_nb, current_airport.get_planes_capacity(), format_amount(sum))

    return HttpResponse(response)
