# -*- coding: utf-8 -*-
# @Time      : 2020-02-06 14:31
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : 字符串连接.py
# @Software  : PyCharm

# 1. +号连接
s1 = "Hello"
s2 = "World"
s = s1 + s2
print(s)

# 2.直接连接
t = "Hello""World"
print(t)

# 3.用逗号(,)连接，标准输出的重定向
# print('Hello', 'World')
# r = 'Hello', 'world'
# print(r)

from io import StringIO
import sys

old_stdout = sys.stdout
result = StringIO()
sys.stdout = result
print('hello', 'world')
sys.stdout = old_stdout  # 恢复标准输出
result_str = result.getvalue()
print("用逗号连接: ", result_str)


class Myclass:
    def __str__(self):
        return 'This is a Myclass Instance.'


my = Myclass()
s = s1 + str(my)
print(s)
