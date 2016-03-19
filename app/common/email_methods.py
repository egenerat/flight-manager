from app.common import constants
from django.core.mail import send_mail


def notify(title, body):
    send_mail(title, body, constants.EMAIL_ADDRESS, [constants.NOTIFY_EMAIL], fail_silently=False)