import unittest

from app.planes.planes_util import duration_mission, calculate_total_consumption_mission,\
    calculate_real_autonomy_one_way


class TestPlanesUtils(unittest.TestCase):
    def test_duration(self):
        distance = 10
        speed = 6
        dur = duration_mission(distance, speed)
        self.assertEqual(2, dur)

    def test_consumption(self):
        duration = 7
        conso_per_hour = 1510
        passengers_nb = 19
        staff_nb = 4
        consumption = calculate_total_consumption_mission(duration, conso_per_hour, passengers_nb, staff_nb)
        self.assertEqual(16579.5, consumption)

    def test_real_autonomy(self):
        kerosene_capacity = 18050
        speed = 922
        conso_per_hour = 1510
        passengers_nb = 19
        staff_nb = 4
        real_autonomy = calculate_real_autonomy_one_way(speed, kerosene_capacity, conso_per_hour, passengers_nb,
                                                        staff_nb)
        self.assertEqual(6454, real_autonomy)

if __name__ == '__main__':
    unittest.main()
