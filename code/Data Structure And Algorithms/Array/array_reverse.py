# -*- coding: utf-8 -*-
# @Time      : 2020-04-19 16:11
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : array_reverse.py
# @Software  : PyCharm
lines = int(input())
nums = []
for line in range(lines):
    num = input()
    nums.append(num)
for i in nums[::-1]:
    print(i)
