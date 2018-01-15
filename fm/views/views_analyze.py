# -*- coding: utf-8 -*-
import json

import re

from app.common.countries import countries
from app.common.target_parse_strings import SHOP_PARSE_MODELS_REGEX
from app.missions.mission_utils import planes_needed_by_category, sort_missions_by_type
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
from fm.models import SupersonicStats

HOURS_PER_WEEK = 168


def view_ideal_supersonic_number(_):
    capacity = 200
    data = SupersonicStats.objects.filter(capacity=capacity)
    lmin = capacity
    lmax = 0
    lmean = 0
    lsum = 0
    for i in data:
        ideal = i.ideal_supersonic_number
        if ideal < lmin:
            lmin = ideal
        if ideal > lmax:
            lmax = ideal
        lsum += ideal
    lmean = lsum / len(data)
    return HttpResponse("""Ideal number of supersonic planes:<br/>
    min: {}<br/>
    max: {}<br/>
    mean: {}<br/><br/>
    Computed over {} measures""".format(lmin, lmax, lmean, len(data)))


def view_top_missions(_):
    mission_list = db_get_ordered_missions_multi_type(200, '-reputation_per_hour')
    nb_planes_needed = planes_needed_by_category(mission_list)
    total_reputation_per_week = 0
    for i in mission_list:
        # approximation, because plane can start a same mission before the previous plane came
        # back from the same mission
        total_reputation_per_week += i.reputation_per_hour * HOURS_PER_WEEK
    return render_to_response('list_missions.html',
                              {
                                  'missions': mission_list,
                                  'planes_needed': nb_planes_needed,
                                  'total_reputation_per_week': int(total_reputation_per_week)
                              })


def view_compare_planes(_):
    result = {"list": []}
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
                # 'engines_nb': spec.get_engine_nb(),
                'consumption': spec.get_kerosene_consumption(),
                'price': spec.get_price()
            })
    return HttpResponse(json.dumps(result), content_type="application/json")


def view_missions_ratios(_):
    result = {}
    mission_list = db_get_ordered_missions_multi_type(400, '-reputation_per_hour')
    sorted_missions = sort_missions_by_type(mission_list)
    for mission_type in sorted_missions:
        min_ratio = 100
        max_ratio = -1
        min_stopover = 100
        max_stopover = -1
        for a_mission in sorted_missions[mission_type]:
            reputation_ratio = a_mission.reputation / float(a_mission.km_nb)
            if not a_mission.stopover:
                if reputation_ratio < min_ratio:
                    min_ratio = reputation_ratio
                if reputation_ratio > max_ratio:
                    max_ratio = reputation_ratio
            else:
                if reputation_ratio < min_stopover:
                    min_stopover = reputation_ratio
                if reputation_ratio > max_stopover:
                    max_stopover = reputation_ratio
        result[mission_type] = {
            'min': min_ratio,
            'max': max_ratio,
            'min_stopover': min_stopover,
            'max_stopover': max_stopover
        }
        # approximation, because plane can start a same mission before the previous
        # plane came back from the same mission
    return HttpResponse(json.dumps(result), content_type="application/json")


def view_list_all_destination_cities(_):
    mission_list = db_get_ordered_missions_multi_type(1000, '-reputation_per_hour')
    result = []
    for i in mission_list:
        if (countries[str(i.country_nb)], i.city_name) not in result:
            result.append((countries[str(i.country_nb)], i.city_name))
    return HttpResponse(json.dumps(result), content_type="application/json")


# TODO cleanup
def planes_value(_):
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
