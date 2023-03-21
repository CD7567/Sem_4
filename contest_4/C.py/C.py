import sys
import functools

def takes(*types):
    def inner(f):
        @functools.wraps(f)
        def decorated(*args, **kwargs):
            for elem in zip(types, args):
                if not isinstance(elem[1], elem[0]):
                    raise TypeError
            return f(*args, **kwargs)
        return decorated
    return inner

exec(sys.stdin.read())