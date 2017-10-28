
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


@default.register(datetime.datetime)
def _(obj):
    r = obj.replace(microsecond=0).isoformat()
    if r.endswith('+00:00'):
        r = r[:-6] + 'Z'
    return r


@default.register(datetime.date)
def _(obj):
    return obj.isoformat()


@default.register(datetime.time)
def _(obj):
    return obj.replace(microsecond=0).isoformat()
