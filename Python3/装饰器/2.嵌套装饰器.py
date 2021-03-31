from tools.print_info import print_info

print_info('装饰器嵌套')


def hello(func):
    def wrapper():
        print("Hello")
        func()

    return wrapper


def welcome(func):
    def wrapper():
        print('Welcome')
        func()

    return wrapper


def say():
    print('Good')


say = hello(welcome(say))
say()

print_info("使用语法糖")


@hello
@welcome
def say2():
    print('You')

say2()