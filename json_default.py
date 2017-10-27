
'''
Implementaion of the ideas from https://hynek.me/articles/serialization/
'''
import datetime
from functools import singledispatch

__version__ = '0.1'


@singledispatch
def default(obj):
    '''Safe and sane default'''
    return str(obj)


@singledispatch.register(datetime.datetime)
def default(obj):
    r = obj.replace(microseconds=0).isoformat()
    if r.endswith('+00:00'):
        r = r[:-6] + 'Z'
    return r


@singledispatch.register(datetime.date)
def default(obj):
    return obj.isoformat()


@singledispatch.register(datetime.time)
def default(obj):
    return obj.replace(microseconds=0).isoformat()
