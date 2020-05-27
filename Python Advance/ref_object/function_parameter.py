# -*- coding: utf-8 -*-
# @Time      : 2020-04-04 16:34
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : function_parameter.py
# @Software  : PyCharm

def f(a, b):
    a += b
    return a


def main():
    x = 1
    y = 2
    print(f(x, y))

    a = [1, 2]
    b = [3, 4]
    print(f(a, b))

    print(a)
    print(b)

    t = (2019, 2020)
    p = (2000, 2004)
    print(f(t, p))

    print(t, p)


if __name__ == '__main__':
    main()
