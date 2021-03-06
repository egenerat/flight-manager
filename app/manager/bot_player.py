# -*- coding: utf-8 -*-
from app.airport import airport_buyer
from app.airport import staff_buyer
from app.airport.airport_builder import build_airport_from_html
from app.airport.airport_checker import AirportChecker
from app.airport.report_parser import report_parser
from app.common.constants import MAIN_AIRPORT_NAME
from app.common.http_methods import get_request
from app.common.target_urls import STAFF_PAGE, AIRPORT_PAGE, MISSION_DASHBOARD, PLANES_PAGE, AIRPORT_REPORT
from app.missions.mission_utils import split_missions_list_by_type
from app.missions.missionparser import subtract, get_ongoing_missions_from_html
from app.parsers.planes_parser import build_planes_from_html
from app.planes.plane_garage import PlaneGarage
from app.planes.planes_util2 import split_planes_list_by_type
from fm.mission_handler import accept_all_missions
from fm.notifications import notify_plane_crashes


def build_airport():
    staff_page = get_request(STAFF_PAGE)
    airport_page = get_request(AIRPORT_PAGE)
    return build_airport_from_html(airport_page, staff_page)


def build_planes():
    html_page = get_request(PLANES_PAGE)
    planes_list = build_planes_from_html(html_page)
    sorted_planes = split_planes_list_by_type(planes_list)
    return sorted_planes


def get_ongoing_missions():
    dashboard = get_request(MISSION_DASHBOARD)
    return get_ongoing_missions_from_html(dashboard)


def build_report():
    report_html = get_request(AIRPORT_REPORT)
    return report_parser(report_html)


class BotPlayer(object):
    def __init__(self, missions):
        self.airport = build_airport()
        self.planes = build_planes()
        self.report = build_report()
        self.missions = missions
        self.available_missions = None
        self.refresh_needed = False

    @property
    def usable_planes(self):
        return self.planes['commercial_ready_planes'] + self.planes['supersonic_ready_planes'] + self.planes[
            'jet_ready_planes']

    @property
    def maintenance_needed_planes(self):
        # should be improved to select only planes with status I
        temp = self.planes['commercial_planes'] + self.planes['supersonic_planes'] + self.planes[
            'jet_planes']
        return [plane for plane in temp if plane.in_mission == 'I' and (plane.required_maintenance or plane.endlife)]

    def launch_missions(self):
        self.refresh_planes()
        self.refresh_available_missions()
        checker = AirportChecker(self.airport, self.planes, airport_buyer, staff_buyer)
        checker.fix()
        self.refresh_needed = checker.refresh_needed

        garage = PlaneGarage(self.usable_planes + self.maintenance_needed_planes, self.airport)
        # garage.get_kerosene_quantity_needed()
        # garage.get_engines_needed_nb()
        garage.prepare_all_planes()
        self.refresh_needed = self.refresh_needed or garage.refresh_needed
        accept_all_missions(self.available_missions, garage.ready_planes)

    def check_report(self):
        daily_report = self.report['daily']
        daily_crashes_number = daily_report['crashes']
        if daily_crashes_number > 0:
            if self.airport.airport_name == MAIN_AIRPORT_NAME:
                notify_plane_crashes(self.airport.airport_name, daily_crashes_number)

    def refresh_planes(self):
        self.planes = build_planes()
        self.refresh_needed = False

    def refresh_available_missions(self):
        mission_list = self.missions
        ongoing_missions = get_ongoing_missions()
        self.available_missions = subtract(mission_list, ongoing_missions)

    def stats_supersonics(self):
        self.refresh_available_missions()
        supersonic_planes = len(self.planes['supersonic_planes'])
        supersonic_missions = len(split_missions_list_by_type(self.missions)['missions_for_supersonics'])
        supersonic_available_missions = len(split_missions_list_by_type(self.available_missions)['missions_for_supersonics'])
        return {
            "capacity": self.airport.planes_capacity,
            "supersonic_planes": supersonic_planes,
            "supersonic_missions": supersonic_missions,
            "supersonic_available_missions": supersonic_available_missions,
            "ideal_supersonic_number": supersonic_available_missions + supersonic_planes
        }
