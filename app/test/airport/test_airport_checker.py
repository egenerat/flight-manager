# -*- coding: iso-8859-1 -*-
from app.airport.airport_checker import amount_needed
import unittest

from app.planes.CommercialPlane import CommercialPlane
from app.planes.JetPlane import JetPlane
from app.planes.SupersonicPlane import SupersonicPlane


class TestAirportParser(unittest.TestCase):

    def test_amount_needed(self):
        missing_planes = {
            CommercialPlane: 1,
            JetPlane: 2,
            SupersonicPlane: 3,
        }
        amount = amount_needed(missing_planes)
        self.assertEqual(amount, 43900000)

if __name__ == '__main__':
    unittest.main()
