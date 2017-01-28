# coding=utf-8
import json

import re

from app.common.target_parse_strings import SHOP_PARSE_MODELS_REGEX
from app.missions.mission_utils import planes_needed_by_category
from app.standalone.PlaneSpecificationParser import PlaneSpecificationParser
from django.shortcuts import render_to_response

from app.airport.Airport import Airport
from app.airport.airports_methods import get_other_airports_id
from app.airport.airports_methods import switch_to_airport
from app.common.http_methods import get_request
from app.common.string_methods import format_amount
from app.common.target_urls import PLANES_PAGE, SHOP_ONE_CONSTRUCTOR_PAGE, SITE
from app.parsers.planes_parser import build_planes_from_html
from django.http import HttpResponse
from fm.databases.database_django import db_get_ordered_missions_multi_type


def view_top_missions(_):
    mission_list = db_get_ordered_missions_multi_type(200, '-reputation_per_hour')
    nb_planes_needed = planes_needed_by_category(mission_list)
    HOURS_PER_WEEK = 168
    total_reputation_per_week = 0
    for i in mission_list:
        # approximation, because plane can start a same mission before the previous plane came back from the same mission
        total_reputation_per_week += i.reputation_per_hour * HOURS_PER_WEEK
    return render_to_response('list_missions.html', {'missions': mission_list,
                                                     'planes_needed': nb_planes_needed,
                                                     'total_reputation_per_week': int(total_reputation_per_week)})


def view_compare_planes(_):
    result = {"list":[]}
    for i in range(1, 9):
        url = SHOP_ONE_CONSTRUCTOR_PAGE.format(shop_constructor_id=i)
        page = get_request(url)
        results = re.findall(SHOP_PARSE_MODELS_REGEX, page)
        for j in results:
            url2 = SITE + "/" + j
            plane_details_html = get_request(url2)
            spec = PlaneSpecificationParser(plane_details_html)
            result['list'].append({
                'plane_model': spec.get_plane_model(),
                'speed': spec.get_speed(),
                'capacity': spec.get_kerosene_capacity(),
                #'engines_nb': spec.get_engine_nb(),
                'consumption': spec.get_kerosene_consumption(),
                'price': spec.get_price()
            })
    return HttpResponse(json.dumps(result), content_type="application/json")


#TODO DEPRECATED
def represent_data(_):
    country_list = ['France', 'Italie', 'Suisse', 'Turquie']
    result = {}
    missions_list = []
    for i in country_list:
        #TODO adapt
        PLANE_CAPACITY = 100
        PLANE_SPEED = 2250
        missions_list = db_get_ordered_missions(i, PLANE_CAPACITY, PLANE_SPEED, 84, '-reputation_per_hour')
        total_reputation_36 = 0
        total_revenue_36 = 0
        total_reputation_54 = 0
        total_revenue_54 = 0
        total_reputation_84 = 0
        total_revenue_84 = 0
        for idx, a_mission in enumerate(missions_list):
            total_revenue_84 += a_mission.revenue_per_hour
            total_reputation_84 += a_mission.reputation_per_hour
            if idx < 54:
                total_revenue_54 += a_mission.revenue_per_hour
                total_reputation_54 += a_mission.reputation_per_hour
            if idx < 36:
                total_revenue_36 += a_mission.revenue_per_hour
                total_reputation_36 += a_mission.reputation_per_hour
        result[i] = {
            'total_reputation_84': total_reputation_84 / 84,
            'total_revenue_84': total_revenue_84 / 84,
            'total_reputation_54': total_reputation_54 / 54,
            'total_revenue_54': total_revenue_54 / 54,
            'total_reputation_36': total_reputation_36 / 36,
            'total_revenue_36': total_revenue_36 / 36,
        }
    return render_to_response('missions.html', {'result': result, 'missions': missions_list})


# TODO cleanup
def planes_value(request):
    response = ''
    other_airports = get_other_airports_id()
    for j in other_airports:
        value_sum = 0
        planes_nb = 0
        switch_to_airport(j)
        current_airport = Airport()
        page = get_request(PLANES_PAGE)
        ready_planes = build_planes_from_html(page)
        for i in ready_planes:
            if i.get_value:
                if i.get_value():
                    value_sum += i.get_value()
                    planes_nb += 1
        response += '{}({}/{}) <br/><br/>'.format(current_airport.airport_name, planes_nb,
                                                  current_airport.planes_capacity, format_amount(value_sum))

    return HttpResponse(response)
