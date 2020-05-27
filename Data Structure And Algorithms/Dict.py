# -*- coding: utf-8 -*-
# @Time      : 2020-04-10 13:29
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : Dict.py
# @Software  : PyCharm

# 现有字典d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}，如何按字典中的值对字典进行排序得到排序后的字典

d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}

d2 = sorted(d.items(), key=lambda k: k[1])

print(dict(d2))

print(sorted(zip(d.values(), d.keys())))
