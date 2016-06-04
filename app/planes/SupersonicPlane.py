
class CommercialPlane(PlaneBean):

    def engines_to_be_changed(self):
        return self.__current_engine_hours >= CHANGE_HOUR_SUPERSONIC

    def get_value(self):
        if self.__km and self.__kerozene:
            return get_concorde_value(self.__km, self.__kerozene)
        return None