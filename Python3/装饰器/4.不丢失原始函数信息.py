from tools.print_info import print_info


def say(func):

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper


@say
def greet(name):
    print("Hello {}".format(name))


print_info("丢失原始函数信息")
print(greet.__name__)

print_info("想要不丢失原始函数信息可以用@functools.wrapper")

import functools
import time


def timer(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        # print(func.__name__)
        # print(run_time)
        print("Finished {} in {} s".format(repr(func.__name__), round(run_time, 3)))
        return value
    return wrapper

@timer
def doubled_and_add(num):
    res = sum([i*2 for i in range(num)])
    print("Result : {}".format((res)))


doubled_and_add(100000)
doubled_and_add(1000000)
