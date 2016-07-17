from app.airport.airport_builder import build_airport
from app.common.http_methods import get_request
from app.common.target_urls import STAFF_PAGE, AIRPORT_PAGE, MISSION_DASHBOARD, PLANES_PAGE
from app.missions.missionparser import get_ongoing_missions, subtract
from app.parsers.planesparser import build_planes_from_html
from app.planes.plane_garage import PlaneGarage
from app.planes.planes_util2 import split_planes_list_by_type
from fm.databases.database import sort_missions_by_type, db_get_ordered_missions_multi_type
from fm.mission_handler import accept_all_missions


class BotPlayer(object):
    def __init__(self):
        self.airport = self.build_airport()
        self.planes = self.build_planes()
        self.ongoing_missions = self.get_ongoing_missions()
        self.missions = self.get_missions()

    def build_airport(self):
        staff_page = get_request(STAFF_PAGE)
        airport_page = get_request(AIRPORT_PAGE)
        return build_airport(airport_page, staff_page)

    def build_planes(self):
        html_page = get_request(PLANES_PAGE)
        planes_list = build_planes_from_html(html_page)
        planes_by_type = split_planes_list_by_type(planes_list)
        return planes_by_type

    def get_ongoing_missions(self):
        dashboard = get_request(MISSION_DASHBOARD)
        return get_ongoing_missions(dashboard)

    def get_mock_missions(self):
        return {1L: [1978L, 1983L, 1973L, 1991L, 1967L, 1958L, 2008L, 1990L, 2000L, 1959L, 1953L], 7L: [1536L, 1535L],
                  12L: [1539L, 1538L, 1537L], 205L: [1916L, 1917L, 1915L, 1914L, 1918L],
                  154L: [2262L, 2276L, 2263L, 2253L, 2264L, 2236L],
                  155L: [1802L, 1805L, 1804L, 1801L, 1807L, 1803L, 1808L, 1806L], 158L: [1820L, 1822L, 1811L],
                  164L: [2853L, 2820L, 2836L, 2864L, 2819L, 2865L, 2835L, 2806L, 2805L, 2859L, 2818L],
                  40L: [1583L, 1587L, 1585L, 1586L, 1588L, 1584L], 41L: [1590L, 1594L, 1596L, 1592L, 1591L],
                  177L: [1872L], 50L: [1624L, 1625L, 1627L, 1623L, 1626L, 1622L],
                  51L: [1881L, 1885L, 1882L, 1878L, 1879L, 1883L, 1880L], 185L: [1898L, 1902L, 1906L, 1903L],
                  62L: [1650L, 1656L, 1652L, 1651L, 1658L, 1654L],
                  63L: [1662L, 1663L, 1660L, 1665L, 1661L, 1666L, 1664L], 68L: [1692L],
                  197L: [1910L, 1909L, 1908L, 1913L, 1907L, 1911L, 1912L], 77L: [2500L, 2488L, 2523L],
                  79L: [1719L, 1722L, 1720L, 1723L, 1721L], 212L: [2154L, 2174L, 2139L, 2145L, 2168L],
                  36L: [2211L, 2204L, 2205L, 2210L, 2223L, 2228L], 227L: [1934L], 102L: [2324L, 2323L],
                  105L: [2723L, 2667L, 2722L, 2692L, 2707L, 2700L, 2713L, 2681L, 2673L, 2660L, 2680L, 2679L],
                  113L: [1767L, 1773L, 1771L, 1774L, 1770L, 1769L, 1768L, 1772L], 114L: [1778L, 1776L, 1775L],
                  121L: [2593L, 2623L, 2610L, 2655L, 2648L]}

    def get_missions(self):
        return sort_missions_by_type(db_get_ordered_missions_multi_type(200, '-reputation_per_hour'))
    ## jet_missions = all_missions['5']

    def launch_missions(self):
        mission_list = self.missions['5']
        ongoing_missions = self.ongoing_missions

        mission_list = subtract(mission_list, ongoing_missions)

        missions_json = {}
        for i in mission_list:
            if i.country_nb not in missions_json:
                missions_json[i.country_nb] = []
            missions_json[i.country_nb].append(i.mission_nb)

        # purge empty countries
        result = {}
        for i in missions_json:
            if missions_json[i]:
                result[i] = missions_json[i]
        jet_list = self.planes['jet_ready_planes']
        ready_planes = jet_list
        PlaneGarage(ready_planes, self.airport).prepare_all_planes()
        accept_all_missions(result, ready_planes)


