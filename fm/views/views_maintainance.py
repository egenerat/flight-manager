
def fill_kero(request):
    # only from market
    fm.singleton_session.session = request.session
    fill_all_airports()
    return HttpResponse('Done')


def start_fill_kero(request):
    taskqueue.add(url='/fm/fill_kero')
    return HttpResponse('Start fill kerozene')


def engines(request):
    fm.singleton_session.session = request.session
    change_engines()
    return 'Done'
