session = None

airport = None

session_to_as = None


def get_airport():
    return airport


def set_airport(current_airport):
    global airport
    airport = current_airport
    
local_mode = True