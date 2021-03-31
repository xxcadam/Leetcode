from tools.print_info import print_info

print_info('*args和**kwargs 接收参数')


def say(func):

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper


@say
def greet(name):
    print("Hello {}".format(name))


greet("xiaojing")


print(greet.__name__)
