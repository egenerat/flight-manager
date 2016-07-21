from django.conf.urls.defaults import *
from fm.views import views_finances
from fm.views import views_test, views_missions


urlpatterns = patterns('fm.views',
    #url(r'^admin/', include(admin.site.urls)),
    # (r'^quizz$', 'quizz'),
    # (r'^answer$', 'answer'),
    # (r'^missions$', 'represent_data'),
    # (r'^refresh$', 'refresh'),
    (r'^start$', views_missions.parse_missions),
    # (r'^stop$', 'stop'),
    (r'^launch_missions$', views_missions.launch_missions),
    (r'^start_launch_missions$', views_missions.start_launch_missions),
    (r'^launch_missions$', views_test.view_launch_missions)
    (r'^taxes$', views_finances.taxes),
    (r'^start_taxes$', views_finances.start_taxes),
    # (r'^sale_airports$', 'sale_airports'),
    # (r'^test$', 'test'),

    # not ready
    # (r'^fill_kero$', 'fill_kero'),
    # (r'^start_fill_kero$', 'start_fill_kero'),
    # (r'^engines$', 'engines'),
)
