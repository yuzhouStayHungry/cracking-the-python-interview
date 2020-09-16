# -*- coding: utf-8 -*-
# @Time      : 2020-09-15 08:33
# @Author    : yuzhou_1su
# @ContactMe : www.yuzhou_1su@163.com
# @File      : time_decorator.py
# @Software  : PyCharm
import time


def time_function(f):
    def wrapper(*args, **kwargs):
        begin = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print("Function call with argument {all_args} took ".format(
            all_args="\t".join((str(args), str(kwargs)))) + str(end - begin) +
              " seconds to execute.")
        return result

    return wrapper


@time_function
def foo():
    print("I am foo()")


@time_function
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

@time_function
def bar(*args, **kwargs):
    print(sum(args) * sum(kwargs.values()))


if __name__ == '__main__':
    foo()
    ackermann(3, 4)
    bar(1, 2, 3, a=2013, b=2014)