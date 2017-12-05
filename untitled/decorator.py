#!/usr/bin/env python
# -*- coding = utf-8 -*-

import functools

def log(text):
    if isinstance(text,str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin %s %s'%(text, func.__name__))
                func(*args,**kw)
                print('end %s %s' % (text, func.__name__))
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('begin %s' % (text.__name__))
            text(*args, **kw)
            print('end %s' % (text.__name__))
        return wrapper

@log('execute')
def now():
    print('2017-6-8')

now()