def taxes(request):
    fm.singleton_session.session = request.session
    money_before_taxes()
    return HttpResponse('Taxes ok!')


def start_taxes(request):
    taskqueue.add(url='/fm/taxes')
    return HttpResponse('Started: taxes')
