import functools
import time

def profiler(func):
    calls = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        nonlocal calls

        if not calls:
            wrapper.calls = 0

        calls += 1
        result = func(*args, **kwargs)
        calls -= 1
        wrapper.calls += 1

        wrapper.last_time_taken = time.time() - start_time
        return result

    return wrapper