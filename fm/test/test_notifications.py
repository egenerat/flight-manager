import unittest

import sys
from unittest.mock import Mock

from datetime import datetime, timedelta

sys.modules['app.common.email_methods'] = Mock()
sys.modules['fm.databases.database_django'] = Mock()
sys.modules['fm.models'] = Mock()
from fm.notifications import should_notify, are_notifications_expired


class MockNotificationModel(object):
    def __init__(self, plane_crashes, last_date):
        self.plane_crashes = plane_crashes
        self.last_date = last_date


class TestNotifications(unittest.TestCase):

    def test_no_existing_notifications(self):
        self.assertEqual(True, should_notify(10, []))
        self.assertEqual(True, should_notify(10, [MockNotificationModel(9, None)]))
        self.assertEqual(False, should_notify(10, [MockNotificationModel(10, None)]))
        self.assertEqual(False, should_notify(10, [MockNotificationModel(11, None)]))

    def test_are_notifications_expired(self):
        self.assertEqual(False, are_notifications_expired([MockNotificationModel(None, datetime.now())]))
        self.assertEqual(True, are_notifications_expired([MockNotificationModel(None,
                                                                                datetime.now() - timedelta(days=2))]))

    # def test_notify_plane_crashes(self):
    #     self.assertEqual(False, should_notify(10, [MockNotificationModel(11, None)]))

if __name__ == '__main__':
    unittest.main()
