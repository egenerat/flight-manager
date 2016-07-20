from app.common.logger import logger
from app.common.email_methods import notify
from app.common.http_methods import get_request, post_request
from app.common.string_methods import string_contains, exception_if_not_contains
from app.common.target_urls import SITE


class PlaneMaintainer(object):

    def __init__(self, plane, airport):
        self.plane = plane
        self.__ready = True
        self.airport = airport
        # TODO make sure airport contains enough resources before maintenance

    def __change_engines(self):
        result = post_request('{}/compte.php?page=action&action=9&id_avion={}'.format(SITE, self.plane.plane_id),
                              {'id_moteur': self.plane.replacement_engines_type})
        if not string_contains("L'avion va bien recevoir ses nouveaux moteurs, dur&eacute;e : 2 heures.", result):
            # TODO parse the answer
            logger.warning('Error while changing engines')
        self.__ready = False

    def __fill_fuel(self):
        fuel_qty = self.plane.fuel_capacity - self.plane.kerozene
        confirm_page = post_request('{}/compte.php?page=action&action=7&id_avion={}'.format(SITE, self.plane.plane_id),
                                    {'cq': fuel_qty})
        if not string_contains('Vous avez ajout&eacute; .+ litres? de k&eacute;ros&egrave;ne dans votre avion !', confirm_page):
            logger.warning('Error when filling fuel')
            self.__ready = False

    def __scrap_plane(self):
        get_request('{}/compte.php?page=action&action=10&id_avion={}'.format(SITE, self.plane.plane_id))

    def __do_maintenance(self):
        page = None
        try:
            page = get_request('{}/compte.php?page=action&action=30&id_avion={}'.format(SITE, self.plane.plane_id))
            exception_if_not_contains('Votre avion est maintenant en maintenance', page)
        except:
            logger.error('Problem sending to maintainance')
            if not string_contains("en mission, en maintenance ou n'a pas plus de 100,000 km sans maintenance",
                                   page):
                # case when the current airport has changed
                # case not enough mecanicians
                notify('AS : could not send to maintainance', page)
            else:
                # TODO case plane maintainance was over, should continue iteration over planes, refresh and run again
                raise OutdatedPlanesListException()

    def prepare_plane(self):
        if self.plane.required_maintenance:
            self.__do_maintenance()
            return False
        if self.plane.engines_to_be_changed():
            self.__change_engines()
            return False
        if not self.plane.is_fuel_full():
            self.__fill_fuel()
        return self.__ready

# TODO: It could be interesting to have a parent class that defines how many engines are required, etc