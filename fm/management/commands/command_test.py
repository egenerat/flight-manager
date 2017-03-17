# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from fm.list_missions import list_dest_countries_id_by_mission_type


class Command(BaseCommand):
    help = 'Test command'

    def handle(self, *args, **options):
        mission_types = ["4", "5"]
        list_dest_countries_id_by_mission_type(mission_types)
        self.stdout.write('Successful')
