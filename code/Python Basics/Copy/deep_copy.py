# -*- coding: utf-8 -*-
# @Time      : 2020-04-06 11:26
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : deep_copy.py
# @Software  : PyCharm

from copy import deepcopy

l1 = [3, [66, 55, 44], (3, 7, 21)]
l2 = list(l1)
l1.append(100)
print('l1:', l1)
print('l2:', l2)
l1[1].remove(55)
l2[1] += [33, 22]
l2[2] += (9, 9, 81)
print('l1:', l1)
print('l2:', l2)
