from tools import print_info as info


info.print_info("手动实现装饰器")
def my_decorator(my_func):

    def my_wrapper():
        print('Before the function runs')

        my_func()

        print('After the function runs')

    return my_wrapper


def my_func():
    print('I am a stand alone function, don\'t you dare modify me')


# my_func()
my_func_decorator = my_decorator(my_func)
my_func_decorator()

info.print_info("语法糖")

# 使用语法糖
@my_decorator
def my_another_func():
    print('Leave me alone')


my_another_func()