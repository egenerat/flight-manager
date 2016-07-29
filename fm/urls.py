# coding=utf-8

from django.conf.urls.defaults import *
from fm.views import views_finances
from fm.views import views_missions
from fm.views import views_test
from fm.views import views_utils
from fm.views import views_watcher

urlpatterns = patterns('fm.views',
                       (r'^parse_missions$', views_missions.view_parse_missions),
                       (r'^launch_missions$', views_missions.view_launch_missions),
                       (r'^launch_missions$', views_missions.view_launch_missions),
                       (r'^taxes$', views_finances.taxes),
                       (r'^watcher$', views_watcher.view_watcher),
                       (r'^start_(?P<view_name>[a-z_]+)$', views_utils.view_generic_async_start),
                       (r'^test$', views_test.view_test),

                       # not ready
                       # (r'^fill_kero$', 'fill_kero'),
                       # (r'^start_fill_kero$', 'start_fill_kero'),
                       # (r'^engines$', 'engines'),

                       # url(r'^admin/', include(admin.site.urls)),
                       # (r'^quizz$', 'quizz'),
                       # (r'^answer$', 'answer'),
                       # (r'^missions$', 'represent_data'),
                       # (r'^refresh$', 'refresh'),
                       # (r'^stop$', 'stop'),
                       )
