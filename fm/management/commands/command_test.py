from fm.bot_player import update_missions
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Update the missions saved in the database'

    def handle(self, *args, **options):
        update_missions()
        self.stdout.write('Successful')
