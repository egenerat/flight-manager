from app.common.constants import NOTIFIED_EMAIL_ADDRESS, EMAIL_ADDRESS
from django.core.mail import send_mail


def notify(title, body):
    send_mail(title, body, EMAIL_ADDRESS, [NOTIFIED_EMAIL_ADDRESS], fail_silently=False)
