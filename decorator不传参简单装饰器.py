import functools

def log(func):
    @functools.wraps(func)
    def wrappers(*args,**kwargs):

        print('begin call %s' % func.__name__)

        return func(*args,**kwargs)
    return wrappers
@log
def foo1():
    print('hello')
@log
def foo2():
    print('how are you?')

foo1()
foo2()