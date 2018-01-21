import functools


def log(func):
    @functools.wraps(func)
    def wraper(*args, **kw):
        print(f'call {func.__name__}')
        func(*args, **kw)

    return wraper



def log_text(text='call'):
    def decorator(func):
        @functools.wraps(func)
        def wraper(*args, **kwargs):
            print(f'{text} {func.__name__}')
            func(*args, **kwargs)

        return wraper

    return decorator


@log_text()
def now():
    print('2017')


if __name__ == '__main__':
    pass
    a = now
    print(a.__name__)
    a()

    b = functools.partial()
    class A:
        pass
    a = A()
    a()
