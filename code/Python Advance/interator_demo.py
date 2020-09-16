# -*- coding: utf-8 -*-
# @Time      : 2020-09-15 08:24
# @Author    : yuzhou_1su
# @ContactMe : www.yuzhou_1su@163.com
# @File      : interator_demo.py
# @Software  : PyCharm

import random


# Iterable object, implement __iter__(), __next__()
class RandomIncrement:

    def __init__(self, limit):
        self._offset = 0.0
        self._limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self._offset += random.random()
        if self._offset > self._limit():
            raise StopIteration
        return self._offset

    def increment_limit(self, increment_amount):
        self._limit += increment_amount


if __name__ == '__main__':
    ri = RandomIncrement(4)

    for r in ri:
        print(r)
