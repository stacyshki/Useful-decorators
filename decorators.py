import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        runtime = end_time - start_time
        print(f'Function completion time is {func.__name__ !r}: {runtime:.4f} secs')
        return value
    return wrapper_timer


def slow(_func=None, *, sec=1):
    def decorator_slower(func):
        @functools.wraps(func)
        def wrapper_slowing_motion():
            time.sleep(sec)
            return func(*args, **kwargs)
        return wrapper_slowing_motion
    if _func is None:
        return decorator_slower
    else:
        return decorator_slower(_func)


def repeat(times):
    def decorator_times(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_times


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.numcalls += 1
        print(f'{wrapper_count_calls.numcalls} function call')
        return func(*args, **kwargs)
    wrapper_count_calls.numcalls = 0
    return wrapper_count_calls


def cache(func):
    @functools.wraps(func)
    def wrapped_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapped_cache.cache:
            wrapped_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapped_cache.cache[cache_key]
    wrapped_cache.cache = dict()
    return wrapped_cache
