def aop(func):
    """aop func"""
    def wrapper(*args, **kwargs):
        """wrapper func"""
        print('before func')
        func(*args, **kwargs)
        print('after func')
    return wrapper


@aop
def hi_with_deco(a):
    """hi func"""
    print('hi' + str(a))


if __name__ == '__main__':
    # hi()
    hi_with_deco(1)