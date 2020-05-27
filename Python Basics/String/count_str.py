# -*- coding: utf-8 -*-
# @Time      : 2020-04-20 12:52
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : count_str.py
# @Software  : PyCharm


# count_dict = {}
# s = input()
# for i in s:
#     if i in count_dict:
#         count_dict[i] += 1
#     else:
#         count_dict[i] = 1
# for k, v in count_dict.items():
#     print(k, end='')
#
# d_order = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
# print(d_order)

# from collections import defaultdict
# dd, s, res = defaultdict(list), input(), ""
# for i in set(s):
#     dd[s.count(i)].append(i)
# for i in sorted(dd.keys(), reverse=True):
#     res += "".join(sorted(dd[i], key=ord))
# print(res)

# n = int(input())
# An = 2 + 3*(n - 1)
# li = [i for i in range(2, An+1, 3)]
# print(li)
# print(sum(li[:n]))

s = 'Jkdi234klowe90a3'
a, res, isNum = input(), "", False

for i in a:
    if i.isdigit():
        if not isNum:
            res = res + "*" + i
        else:
            res += i
        isNum = True
    else:
        if isNum:
            res = res + '*' + i
        else:
            res += i
        isNum = False
if a[-1].isdigit():
    res += '*'

print(res)
