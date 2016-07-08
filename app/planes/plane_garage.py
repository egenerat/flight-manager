from app.planes.plane_maintainer import PlaneMaintainer


class PlaneGarage(object):

    def __init__(self, plane_list, airport):
        self.plane_list = plane_list
        self.airport = airport
        # TODO make sure airport contains enough resources before maintenance

    def prepare_all_planes(self):
        for i in self.plane_list:
            PlaneMaintainer(i, self.airport).prepare_plane()

# TODO: It could be interesting to have a parent class that handles all the planes, and define how many engines are required, etc