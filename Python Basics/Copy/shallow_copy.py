# -*- coding: utf-8 -*-
# @Time      : 2020-04-06 08:32
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : shallow_copy.py
# @Software  : PyCharm


import copy
import functools


@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name


def main():
    a = MyClass('a')
    my_list = [a]
    dup = copy.copy(my_list)

    print('my_list:{}'.format(my_list))
    print('dup:', dup)
    print('dup is my_list:', (dup is my_list))
    print('dup == my_list:', (dup == my_list))
    print('dup[0] is my_list[0]:', (dup[0] is my_list[0]))
    print('dup[0] == my_list[0]:', (dup[0] == my_list[0]))


if __name__ == '__main__':
    main()
