# coding=utf-8

from django.conf.urls.defaults import *
from fm.views import views_utils
from fm.views.views_analyze import view_top_missions, view_compare_planes
from fm.views.views_missions import view_empty_db_missions

urlpatterns = patterns('fm.views',
                       (r'^start_(?P<view_name>[a-z_]+)$', views_utils.view_generic_async_start),
                       (r'^(?P<view_name>(\blaunch_missions\b)|(\bparse_missions\b)|(\btaxes\b)|(\bwatcher\b))$', views_utils.view_generic),
                       # For the view that do not require session with the remote server
                       (r'^top_missions$', view_top_missions),
                       (r'^empty_db_missions', view_empty_db_missions),
                       (r'^compare_planes', view_compare_planes)
                       )
