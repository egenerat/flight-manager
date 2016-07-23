from app.common.as_exceptions import OutdatedPlanesListException
from app.common.logger import logger
from app.common.email_methods import notify
from app.common.http_methods import get_request, post_request
from app.common.string_methods import string_contains, exception_if_not_contains
from app.common.target_urls import CHANGE_ENGINES_URL, FILL_FUEL_URL, SCRAP_PLANE_URL, MAINTENANCE_URL


class PlaneMaintainer(object):
    def __init__(self, plane, airport):
        self.plane = plane
        self.__ready = True
        self.airport = airport
        # TODO make sure airport contains enough resources before maintenance

    def __change_engines(self):
        result = post_request(CHANGE_ENGINES_URL.format(plane_id=self.plane.plane_id),
                              {'id_moteur': self.plane.replacement_engines_type})
        if not string_contains("L'avion va bien recevoir ses nouveaux moteurs, dur&eacute;e : 2 heures.", result):
            # TODO parse the answer
            logger.warning('Error while changing engines')
        self.__ready = False

    def __fill_fuel(self):
        fuel_qty = self.plane.fuel_capacity - self.plane.kerosene
        confirm_page = post_request(FILL_FUEL_URL.format(plane_id=self.plane.plane_id),
                                    {'cq': fuel_qty})
        if not string_contains('Vous avez ajout&eacute; .+ litres? de k&eacute;ros&egrave;ne dans votre avion !',
                               confirm_page):
            logger.warning('Error when filling fuel')
            self.__ready = False

    def __scrap_plane(self):
        get_request(SCRAP_PLANE_URL.format(plane_id=self.plane.plane_id))

    def __do_maintenance(self):
        page = None
        try:
            page = get_request(MAINTENANCE_URL.format(plane_id=self.plane.plane_id))
            exception_if_not_contains('Votre avion est maintenant en maintenance', page)
        except:
            logger.error('Problem sending to maintenance')
            if not string_contains("en mission, en maintenance ou n'a pas plus de 100,000 km sans maintenance",
                                   page):
                # case when the current airport has changed
                # case not enough mecanicians
                notify('FM : could not send to maintenance', page)
            else:
                # TODO case plane maintenance was over, should continue iteration over planes, refresh and run again
                raise OutdatedPlanesListException()
        self.__ready = False

    def prepare_plane(self):
        if self.plane.endlife:
            self.__scrap_plane()
        if self.plane.required_maintenance:
            self.__do_maintenance()
            return False
        if self.plane.engines_to_be_changed():
            self.__change_engines()
            return False
        if not self.plane.is_fuel_full():
            self.__fill_fuel()
        return self.__ready
