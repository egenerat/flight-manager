from datetime import datetime

from app.common.email_methods import notify
from fm.databases.database_django import db_get_all_notifications, remove_all_notifications
from fm.models import Notification


def should_notify():
    pass


def are_notifications_expired():
    return False


def notify_plane_crashes(airport_name, daily_crashes_number):
    if are_notifications_expired():
        remove_all_notifications()
    notif = Notification(last_date=datetime.now(), plane_crashes=daily_crashes_number)
    existing_notifications = db_get_all_notifications()
    if notif:
        pass
    message = '{}: {} crashes'.format(airport_name, daily_crashes_number)
    notify(message, message)