from app.common.email_methods import notify
from django.core.management.base import BaseCommand
from fm.bot_player import send_planes
from app.common.logger import logger
import traceback


class Command(BaseCommand):
    help = 'Launch all missions'

    def handle(self, *args, **options):
        try:
            send_planes()
            logger.info('Successful')
        except Exception as e:
            exception_text = traceback.format_exc()
            logger.error(exception_text)
            notify('AS : There was a bug during execution',
                      'There was a bug during execution :\n' + str(exception_text))
            logger.info('Failure')
