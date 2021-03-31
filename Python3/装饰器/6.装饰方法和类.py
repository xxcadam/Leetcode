import functools
import time
from tools.print_info import print_info


print_info("装饰方法")


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


class Calculator:

    def __init__(self, num):
        self.num = num

    @timer
    def doubled_and_add(self):
        res = sum([i * 2 for i in range(self.num)])
        print("Result : {}".format(res))


c = Calculator(10000)
c.doubled_and_add()


print_info("装饰类")


@timer
class Calculator2:

    def __init__(self, num):
        self.num = num
        time.sleep(2)

    def doubled_and_add(self):
        res = sum([i * 2 for i in range(self.num)])
        print("Result : {}".format(res))


print(Calculator2(100))