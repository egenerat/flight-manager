# coding=utf-8
from app.common.string_methods import get_value_from_regex, get_amount


class PlaneSpecificationParser(object):

    def __init__(self, *args):
        self.html_page = args.pop('html_page')

    def get_plane_model(self):
        return get_value_from_regex("""<span class="titre">Fiche détaillée de l'avion : (.+?)</span>""", self.html_page)

    def get_speed(self):
        return get_amount(get_value_from_regex('<td class="fiche1">Vitesse de croisière</td>[\n\s]+<td class="fiche2">(.+) Km/h</td>', self.html_page))

    def get_kerosene_capacity(self):
        return get_amount(get_value_from_regex("""<td class="fiche1">Capacité maximale de carburant</td>[\n\s]+<td class="fiche2">(.+) litres</td>""", self.html_page))

    def get_engine_nb(self):
        return get_value_from_regex("""<td class="fiche1">Poussée</td>[\n\s]+<td class="fiche2">(\d+) x .+ kN</td>""", self.html_page)

    def get_kerosene_consumption(self):
        return get_amount(get_value_from_regex("""<td class="fiche1">Consommation (des moteurs)</td>[\n\s]+<td class="fiche2">(.+) litres/heure</td>""", self.html_page))

    def get_price(self):
        return get_amount(get_value_from_regex("""<td class="fiche1">Prix</td>[\n\s]+<td class="fiche2">(.+) $</td>""", self.html_page))
