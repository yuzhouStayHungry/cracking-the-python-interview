# -*- coding: utf-8 -*-
# @Time      : 2020-03-30 16:31
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : change_money.py
# @Software  : PyCharm


t = [100, 50, 20, 5, 1]


def change_money(t, n):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
    return m, n


print(change_money(t, 497))
