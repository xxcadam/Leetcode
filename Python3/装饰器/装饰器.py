import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        print(**kwargs)
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print("Finished {} in {} s".format(repr(func.__name__), round(run_time, 3)))
        return value

    return wrapper


@timer
def doubled_and_add(num):
    res = sum([i * 2 for i in range(num)])
    print("Result : {}".format(res))


doubled_and_add(100000)
doubled_and_add(1000000)
# outputs:
# Result : 9999900000
# Finished ‘doubled_and_add’ in 0.0119 s
# Result : 999999000000
# Finished ‘doubled_and_add’ in 0.0897 s