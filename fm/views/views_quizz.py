# coding=utf-8

import re

import fm
from app.common.http_methods import get_request
from app.common.target_urls import URL_CHAT_ENABLE, URL_CHAT
from app.quizz.main_quizz_answer import parse
from app.quizz.quizz_methods import get_quizz_body_content
from django.shortcuts import render_to_response, redirect


def quizz(request):
    fm.singleton_session.session = request.session
    r = get_request(URL_CHAT)
    if len(re.findall('Pour revenir sur la taverne', r)):
        get_request(URL_CHAT_ENABLE)
        r = get_request(URL_CHAT)
    content = get_quizz_body_content(r)
    return render_to_response('quizz.html', {'chat': content})


def answer(request):
    fm.singleton_session.session = request.session
    parse()
    return redirect('/fm/quizz')
