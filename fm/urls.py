# coding=utf-8

from django.conf.urls.defaults import *
from fm.views import views_utils

urlpatterns = patterns('fm.views',
                       (r'^start_(?P<view_name>[a-z_]+)$', views_utils.view_generic_async_start),
                       (r'^(?P<view_name>(\blaunch_missions\b)|(\bparse_missions\b)|(\btaxes\b)|(\bwatcher\b))$', views_utils.view_generic),
                       )
