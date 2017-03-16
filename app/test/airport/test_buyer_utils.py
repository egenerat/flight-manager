# -*- coding: utf-8 -*-
import unittest

from app.airport.buyer_utils import amount_needed
from app.planes.commercial7plane4 import Commercial7Plane4
from app.planes.jet_ds_plane import JetDSPlane
from app.planes.supersonic_cc_plane import SupersonicCCPlane


class TestBuyerUtils(unittest.TestCase):

    def test_amount_needed(self):
        missing_planes = {
            Commercial7Plane4: 1,
            JetDSPlane: 2,
            SupersonicCCPlane: 3,
        }
        amount = amount_needed(missing_planes)
        self.assertEqual(43900000, amount)

if __name__ == '__main__':
    unittest.main()
