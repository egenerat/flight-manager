# coding=utf-8

from django.db import models
import base64


class Mission(models.Model):
    expiry_date = models.DateTimeField()
    origin_country = models.CharField(max_length=30, blank=True)
    country_nb = models.PositiveSmallIntegerField()
    mission_nb = models.PositiveSmallIntegerField()
    travellers_nb = models.PositiveSmallIntegerField()
    contract_amount = models.PositiveIntegerField()
    reputation = models.PositiveSmallIntegerField()
    pilots_nb = models.PositiveSmallIntegerField()
    flight_attendants_nb = models.PositiveSmallIntegerField()
    time_before_departure = models.PositiveSmallIntegerField()
    km_nb = models.PositiveSmallIntegerField()
    total_time = models.PositiveSmallIntegerField(null=True)
    revenue_per_hour = models.PositiveSmallIntegerField(null=True)
    reputation_per_hour = models.FloatField(null=True)
    mission_type = models.CharField(max_length=1)
    stopover = models.OneToOneField('Stopover', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Mission {}".format(self.mission_nb)


class Stopover(models.Model):
    revenue = models.PositiveSmallIntegerField(null=True)
    reputation = models.PositiveSmallIntegerField(null=True)
    travellers_nb = models.PositiveSmallIntegerField(max_length=1)


class AirportsToBeSold(models.Model):
    airport_id = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()
    cash = models.SmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
    reputation = models.PositiveSmallIntegerField()


class Notification(models.Model):
    last_date = models.DateTimeField()
    plane_crashes = models.PositiveSmallIntegerField()


class ASHttpSession(models.Model):
    _data = models.TextField(
        db_column='data',
        blank=True)

    def set_data(self, data):
        self._data = base64.encodestring(data)

    def get_data(self):
        return base64.decodestring(self._data)

    data = property(get_data, set_data)
