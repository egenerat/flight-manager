from django.http import HttpResponse


def view_test(request):
    return HttpResponse('test: OK')
