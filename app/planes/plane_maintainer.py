# coding=utf-8
from app.common.constants import MAIN_AIRPORT_NAME
from app.common.constants_strategy import SUPERSONIC_MODEL_TO_BE_PURCHASED, JET_MODEL_TO_BE_PURCHASED, \
    COMMERCIAL_MODEL_TO_BE_PURCHASED
from app.common.logger import logger
from app.common.email_methods import notify
from app.common.http_methods import get_request, post_request
from app.common.string_methods import string_contains, exception_if_not_contains, get_values_from_regex
from app.common.target_strings import ALLIANCE_PUT_PLANE_SUCCESSFUL
from app.common.target_urls import CHANGE_ENGINES_URL, FILL_FUEL_URL, SCRAP_PLANE_URL, MAINTENANCE_URL, \
    ALLIANCE_PUT_PLANE, ALLIANCE_PAGE, SITE
from app.planes.commercial_plane import CommercialPlane
from app.planes.jet_plane import JetPlane
from app.planes.supersonic_plane import SupersonicPlane


class PlaneMaintainer(object):
    def __init__(self, plane, airport):
        self.plane = plane
        self.__ready = True
        self.airport = airport
        # TODO make sure airport contains enough resources before maintenance

    def __change_engines(self):
        result = post_request(CHANGE_ENGINES_URL.format(plane_id=self.plane.plane_id),
                              {'id_moteur': self.plane.replacement_engines_type})
        if not string_contains(u"L'avion va bien recevoir ses nouveaux moteurs, durée : 2 heures.", result):
            # TODO parse the answer
            logger.warning('Error while changing engines')
        self.__ready = False

    def __fill_fuel(self):
        fuel_qty = self.plane.fuel_capacity - self.plane.kerosene
        confirm_page = post_request(FILL_FUEL_URL.format(plane_id=self.plane.plane_id),
                                    {'cq': fuel_qty})
        if not string_contains(u'Vous avez ajouté .+ litres? de kérosène dans votre avion !',
                               confirm_page):
            logger.warning('Error when filling fuel')
            self.__ready = False

    def __scrap_plane(self):
        get_request(SCRAP_PLANE_URL.format(plane_id=self.plane.plane_id))
        self.__ready = False

    def __do_maintenance(self):
        page = None
        try:
            page = get_request(MAINTENANCE_URL.format(plane_id=self.plane.plane_id))
            exception_if_not_contains(u'Votre avion est maintenant en maintenance', page)
        except:
            logger.error('Problem sending to maintenance')
            if not string_contains(u"en mission, en maintenance ou n'a pas plus de 100,000 km sans maintenance",
                                   page):
                # case when the current airport has changed
                # case not enough mecanicians
                notify('FM : could not send to maintenance', page)
            else:
                # TODO case plane maintenance was over, should continue iteration over planes, refresh and run again
                logger.warning("Outdated plane list (not an exception anymore)")
                # raise OutdatedPlanesListException()
        self.__ready = False

    def prepare_plane(self):
        # if self.airport.airport_name == MAIN_AIRPORT_NAME:
        #     self.removing_planes()
        # else:
        #     self.removing_planes_minor_airports()
        if self.plane.endlife:
            self.__scrap_plane()
            return False
        if self.plane.required_maintenance:
            self.__do_maintenance()
            return False
        if self.plane.engines_to_be_changed():
            self.__change_engines()
            return False
        if not self.plane.is_fuel_full():
            self.__fill_fuel()
        return self.__ready

    def removing_planes(self):
        if isinstance(self.plane, SupersonicPlane) and not isinstance(self.plane, SUPERSONIC_MODEL_TO_BE_PURCHASED):
            put_plane_alliance(self.plane.plane_id)
        elif isinstance(self.plane, JetPlane) and not isinstance(self.plane, JET_MODEL_TO_BE_PURCHASED):
            put_plane_alliance(self.plane.plane_id)
        elif isinstance(self.plane, CommercialPlane) and not isinstance(self.plane, COMMERCIAL_MODEL_TO_BE_PURCHASED):
            put_plane_alliance(self.plane.plane_id)

    def removing_planes_minor_airports(self):
        if isinstance(self.plane, SupersonicPlane) and isinstance(self.plane, SUPERSONIC_MODEL_TO_BE_PURCHASED):
            put_plane_alliance(self.plane.plane_id)
        elif isinstance(self.plane, JetPlane) and isinstance(self.plane, JET_MODEL_TO_BE_PURCHASED):
            put_plane_alliance(self.plane.plane_id)
        elif isinstance(self.plane, CommercialPlane) and isinstance(self.plane, COMMERCIAL_MODEL_TO_BE_PURCHASED):
            put_plane_alliance(self.plane.plane_id)


def put_plane_alliance(plane_id):
    response = post_request(ALLIANCE_PUT_PLANE, {'cq': 1, 'la_variete': str(plane_id)})
    return ALLIANCE_PUT_PLANE_SUCCESSFUL in response


def take_planes_alliance(nb_planes_required):
    alliance_page = get_request(ALLIANCE_PAGE)
    available_plane_types = get_values_from_regex(u'<a href="(.*)" class="lien">Détails</a>', alliance_page)
    planes_available = []
    for plane_type in available_plane_types:
        page = get_request('{}/{}'.format(SITE, plane_type))
        planes_available = get_values_from_regex(u'<a href="(.*)" class="lien">Retirer</a>', page)
    nb_planes_available = len(planes_available)
    for i in range(0, min(nb_planes_required, nb_planes_available)):
        get_request('{}/{}'.format(SITE, planes_available[i]))
