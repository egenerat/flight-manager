# -*- coding: iso-8859-15 -*-

import pickle
import fm.singleton_session
from fm.models import ASHttpSession


# TODO
def save_to_session(content):
    pass


def force_save_session_to_db():
    content = fm.singleton_session.session_to_as
    ASHttpSession.objects.all().delete()
    a_string = pickle.dumps(content)
    session = ASHttpSession()
    session.data = a_string
    session.save()


def save_to_file(content):
    # def save_to_file(content, filename):
    #     f = open(filename, 'wb')
    #     pickle.dump(content, f)
    #     f.close()
    # fm.singleton_session.session['login'] = content
    # V2 ========================
    # ASHttpSession.objects.all().delete()
    # a_string = pickle.dumps(content)
    # session = ASHttpSession()
    # session.data = a_string
    # session.save()
    fm.singleton_session.session_to_as = content


def login_exists():
    #     return 'login' in fm.singleton_session.session  
    # return ASHttpSession.objects.count() > 0
    return len(ASHttpSession.objects.all()) > 0


def read_login_file():
    #      exist = os.path.isfile(SAVED_SESSION)
    #     if exist:
    #         return read_from_file(SAVED_SESSION)
    #     return None
    #     f = open(filename, 'rb')
    #     content = pickle.load(f)
    #     f.close()
    in_memory = fm.singleton_session.session_to_as
    if in_memory:
        return in_memory
    if login_exists():
        return pickle.loads(ASHttpSession.objects.all()[0].data)
    else:
        return None
