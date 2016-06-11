# -*- coding: utf-8 -*-
import re
import traceback
from app.airport.Airport import Airport
from app.common.email_methods import notify
from app.common.target_urls import PLANES_PAGE, SITE, URL_CHAT, URL_CHAT_ENABLE

from app.planes.deserialization import build_planes_from_html
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from app.airport.airports_methods import money_before_taxes, switch_to_airport, get_other_airports_id
from app.common.constants import CONCORDE_SPEED, CONCORDE_CAPACITY
from app.common.logger import logger
from app.common.string_methods import format_amount
from app.quizz.main_quizz_answer import parse, get_quizz_body_content
from fm.bot_player import send_planes
from fm.bot_player import update_missions
from fm.fill_kero import fill_all_airports
import fm.singleton_session
from google.appengine.api import taskqueue
from fm.database import db_get_ordered_missions
from app.common.http_methods import get_request
from app.manager.prepare_planes import change_engines_if_needed
from app.parsers.planesparser import build_planes_from_html
from app.planes.planes_util2 import split_planes_list_by_type


def engines(request):
    fm.singleton_session.session = request.session
    html_page = get_request(PLANES_PAGE)
    planes_list = build_planes_from_html(html_page)
    split_list = split_planes_list_by_type(planes_list)
    commercial_list = split_list['commercial_planes']
    change_engines_if_needed(commercial_list)
    return 'Done'


def test(request):
    response = ''
    fm.singleton_session.session = request.session
    other_airports = get_other_airports_id()
    for j in other_airports:
        sum = 0
        planes_nb = 0
        switch_to_airport(j)
        current_airport = Airport()
        page = get_request(PLANES_PAGE)
        ready_planes = build_planes_from_html(page, True)
        for i in ready_planes:
            if i.get_value:
                if i.get_value():
                    sum += i.get_value()
                    planes_nb += 1
        response += current_airport.get_airport_name() + '('+str(planes_nb)+'/'+ str(current_airport.get_planes_capacity())+'): ' + format_amount(sum) + '<br/><br/>'
    return HttpResponse(response)


def taxes(request):
    fm.singleton_session.session = request.session
    money_before_taxes()
    return HttpResponse('Taxes ok!')


def start_taxes(request):
    taskqueue.add(url='/fm/taxes')
    return HttpResponse('Started: taxes')


def launch_missions(request):
    fm.singleton_session.session = request.session
    try:
        send_planes()
        logger.info('Successful')
    except Exception as e:
        exception_text = traceback.format_exc()
        logger.error(exception_text)
        notify('AS : There was a bug during execution', 'There was a bug during execution :\n'+str(exception_text))
#         taskqueue.add(url='/fm/launch_missions', countdown=60*30)
    return HttpResponse('started')


def start_launch_missions(request):
    purge_queue()
    taskqueue.add(url='/fm/launch_missions')
    return HttpResponse('Started: launch missions')


def start(request):
    taskqueue.add(url='/fm/refresh')
    return HttpResponse('Started')


def purge_queue():
    q = taskqueue.Queue('default')
    q.purge()


def stop(request):
    purge_queue()
    return HttpResponse('Stopped')


def refresh(request):
    fm.singleton_session.session = request.session
    update_missions()
    return HttpResponse('Refresh done')


def fill_kero(request):
    # only from market
    fm.singleton_session.session = request.session
    fill_all_airports()
    return HttpResponse('Done')


def start_fill_kero(request):
    taskqueue.add(url='/fm/fill_kero')
    return HttpResponse('Start fill kerozene')


def quizz(request):
    fm.singleton_session.session = request.session
    r = get_request(URL_CHAT)
    if len(re.findall('Pour revenir sur la taverne', r)):
        get_request(URL_CHAT_ENABLE)
        r = get_request(URL_CHAT)
    content = get_quizz_body_content(r)
    return render_to_response('quizz.html', {'chat':content})


def answer(request):
    fm.singleton_session.session = request.session
    parse()
    return redirect('/fm/quizz')


def represent_data(request):
    country_list = ['France', 'Italie', 'Suisse', 'Turquie']
    result = {}
    missions_list = []
    for i in country_list:
        missions_list = db_get_ordered_missions(i, CONCORDE_CAPACITY, CONCORDE_SPEED, 84, '-reputation_per_hour')
        total_reputation_36 = 0
        total_revenue_36 = 0
        total_reputation_54 = 0
        total_revenue_54 = 0
        total_reputation_84 = 0
        total_revenue_84 = 0
        for idx,a_mission in enumerate(missions_list):
            total_revenue_84 += a_mission.revenue_per_hour
            total_reputation_84 += a_mission.reputation_per_hour
            if idx < 54:
                total_revenue_54 += a_mission.revenue_per_hour
                total_reputation_54 += a_mission.reputation_per_hour
            if idx < 36:
                total_revenue_36 += a_mission.revenue_per_hour
                total_reputation_36 += a_mission.reputation_per_hour
        result[i] = {
                     'total_reputation_84':total_reputation_84/84,
                       'total_revenue_84':total_revenue_84/84,
                     'total_reputation_54':total_reputation_54/54,
                       'total_revenue_54':total_revenue_54/54,
                       'total_reputation_36':total_reputation_36/36,
                       'total_revenue_36':total_revenue_36/36,
                     }
    print(result)
    return render_to_response('missions.html',{'result':result,
                                               'missions':missions_list
                                              })