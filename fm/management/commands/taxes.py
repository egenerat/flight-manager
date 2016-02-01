from django.core.management.base import BaseCommand
from app.airport.airports_methods import money_before_taxes


class Command(BaseCommand):
    help = 'Empty bank accounts'

    def handle(self, *args, **options):
        money_before_taxes()
        self.stdout.write('Successful')
