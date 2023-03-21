import functools
from collections import OrderedDict

def cache(n):
    last_calls = OrderedDict()

    def inner(func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            if args in last_calls.keys():
                last_calls.move_to_end(args, last = True)
            else:
                last_calls[args] = func(*args, **kwargs)

            if len(last_calls.keys()) > n:
                last_calls.popitem(last = False)

            return last_calls[args]
        return decorated
    return inner