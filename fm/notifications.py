from app.common.email_methods import notify
from fm.databases.database_django import db_get_all_notifications, remove_all_notifications, db_insert_object
from fm.models import Notification
from datetime import datetime, timedelta


def should_notify(daily_crashes_number, existing_notifications):
    result = False
    if len(existing_notifications):
        latest_notification = existing_notifications[0]
        if daily_crashes_number > latest_notification.plane_crashes:
            result = True
    else:
        result = True
    return result


def get_report_reset_time():
    yesterday = datetime.today() - timedelta(days=1)
    yesterday.replace(hour=23)
    return yesterday


# needs to be reset at the same time the crash counter is reset
def are_notifications_expired(existing_notifications):
    reset_datetime = get_report_reset_time()
    if len(existing_notifications):
        latest_notification = existing_notifications[0]
        if latest_notification.last_date < reset_datetime:
            return True
    return False


def notify_plane_crashes(airport_name, daily_crashes_number):
    existing_notifications = db_get_all_notifications()
    if are_notifications_expired():
        remove_all_notifications()
    if should_notify(daily_crashes_number, existing_notifications):
        message = '{}: {} crashes'.format(airport_name, daily_crashes_number)
        notify(message, message)
        current_notification = Notification(last_date=datetime.now(), plane_crashes=daily_crashes_number)
        db_insert_object(current_notification)
