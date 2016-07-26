# coding=utf-8

from django.core.management.base import BaseCommand
from fm.list_missions import list_countries


class Command(BaseCommand):
    help = 'Update the missions saved in the database'

    def handle(self, *args, **options):
        list_countries()
        self.stdout.write('Successful')
