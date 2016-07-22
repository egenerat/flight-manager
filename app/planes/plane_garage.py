from app.planes.plane_maintainer import PlaneMaintainer


class PlaneGarage(object):
    def __init__(self, plane_list, airport):
        self.plane_list = plane_list
        self.airport = airport

    def prepare_all_planes(self):
        temp_ready_planes = []
        for i in self.plane_list:
            is_ready = PlaneMaintainer(i, self.airport).prepare_plane()
            # if returns false, remove from the list
            if is_ready:
                temp_ready_planes.append(i)
        self.ready_planes = temp_ready_planes

    def get_engines_needed_nb(self):
        result = {}
        for i in self.plane_list:
            if i.engines_to_be_changed():
                if i.replacement_engines_type in result:
                    result[i.replacement_engines_type] += i.engines_nb
                else:
                    result[i.replacement_engines_type] = i.engines_nb
        return result

    def get_kerosene_quantity_needed(self):
        result = 0
        for i in self.plane_list:
            if not i.is_fuel_full():
                result += i.fuel_capacity - i.kerosene
        return result

    #TODO
    # def buy_missing_planes(self):
    #     full_planes_nb = self.get_planes_capacity()
    #     missing_planes = full_planes_nb - self.get_planes_nb()
    #     if missing_planes > 0:
    #         try:
    #             self.buy_missing_concorde(missing_planes)
    #         except Exception as e:
    #             logger.error('Could not buy Concorde !')
    #             notify('Errror AS : Could not buy a Concorde {}\nCould not buy a concorde\n{}'.format(get_airport().get_airport_name(), unicode(e)))
