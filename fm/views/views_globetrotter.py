# -*- coding: utf-8 -*-

import copy

from app.analyzer.globetrotter import Globetrotter, simulate_reputation_mission, filter_top_n_missions
from app.analyzer.location import Location
from app.analyzer.location_coordinates import distance_2_points
from app.common.countries import countries
from app.missions.mission_utils import is_possible_mission, find_plane_class_for_mission
from app.planes.planes_util import duration_mission_one_way
from django.shortcuts import render_to_response

from fm.databases.database_django import db_get_ordered_missions_multi_type

HOURS_PER_WEEK = 168


def view_globetrotter(_):
    mission_list = db_get_ordered_missions_multi_type(10000, '-reputation_per_hour')
    globetrotter = Globetrotter()
    fr_loc = Location()
    origin_dict = globetrotter.get_origin_airports_location()
    countries_list = []

    # DEBUG
    emirates_missions = []
    emirates_total_reputation = 0
    for an_origin in origin_dict:
        total_reputation_country = 0
        jet_nb = 0
        supersonic_nb = 0
        stopover_nb = 0
        possible_missions = []
        origin_loc = origin_dict.get(an_origin)
        for a_mission in mission_list:
            a_destination_loc = fr_loc.get_location(a_mission.city_name, countries.get(str(a_mission.country_nb)))
            if a_destination_loc and origin_loc:
                simulated_distance = distance_2_points(origin_loc, a_destination_loc)
                clone_mission = copy.deepcopy(a_mission)
                clone_mission.km_nb = simulated_distance
                if is_possible_mission(clone_mission):
                    simulated_reputation = simulate_reputation_mission(
                        clone_mission.mission_type,
                        clone_mission.stopover is not None,
                        clone_mission.km_nb
                    )
                    simulated_duration = duration_mission_one_way(
                        clone_mission.km_nb,
                        find_plane_class_for_mission(clone_mission).speed
                    ) * 2 + clone_mission.time_before_departure + 1
                    clone_mission.reputation = simulated_reputation
                    clone_mission.reputation_per_hour = simulated_reputation / float(simulated_duration)
                    clone_mission.total_time = simulated_duration
                    possible_missions.append((clone_mission, clone_mission.reputation_per_hour))
        country, city = an_origin
        top_missions = filter_top_n_missions(possible_missions, 200)
        for a_mission, reputation_per_hour in top_missions:
            total_reputation_country += a_mission.reputation_per_hour * HOURS_PER_WEEK
            if a_mission.mission_type == '4':
                supersonic_nb += 1
            elif a_mission.mission_type == '5':
                jet_nb += 1
            if a_mission.stopover:
                stopover_nb += 1
        countries_list.append((country, int(total_reputation_country), len(possible_missions), supersonic_nb, jet_nb, stopover_nb))
        if an_origin[0] == 'Émirats Arabes Unis':
            emirates_total_reputation = int(total_reputation_country)
            for mission, reput in top_missions:
                emirates_missions.append(mission)
    # return render_to_response('list_missions.html',
    #                               {
    #                                   'missions': emirates_missions,
    #                                   'planes_needed': {},
    #                                   'total_reputation_per_week': emirates_total_reputation
    #                               })
    countries_list.sort(key=lambda tup: tup[1], reverse=True)
    return render_to_response('list_origin_countries.html', {'countries_list': countries_list})
