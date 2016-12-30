# coding=utf-8

from django.core.management.base import BaseCommand
from fm.list_missions import list_dest_countries_id_by_mission_type


class Command(BaseCommand):
    help = 'Test command'

    def handle(self, *args, **options):
        list_dest_countries_id_by_mission_type()
        self.stdout.write('Successful')
