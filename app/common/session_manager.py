# coding=utf-8

import fm
from fm.databases.database_django import read_session_from_db, is_session_in_db


def get_session():
    cached_session = fm.singleton_session.session_to_as
    if cached_session:
        return cached_session
    elif is_session_in_db():
        database_session = read_session_from_db()
        fm.singleton_session.session_to_as = database_session
        return database_session


def save_session_in_cache(session):
    fm.singleton_session.session_to_as = session

