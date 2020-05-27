# -*- coding: utf-8 -*-
# @Time      : 2020-04-14 21:35
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : primer.py
# @Software  : PyCharm

def getResult(num):
    isPrimer = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            isPrimer = 0
            print(str(i), end=' ')
            getResult(int(num / i))
            break
    if isPrimer == 1:
        print(str(num), end=' ')
#
# getResult(180)

# def getResult2(num):
#     # l = []
#     while num != 1:
#         for i in range(2, int(num) + 1):
#             if num % i == 0:
#                 # l.append(i)
#                 print(i, end=' ')
#                 num = num / i
#                 break
# getResult2(200)

# num = int(input())
# while num != 1:
#     for i in range(2, num + 1):
#         if num % i == 0:
#             print(i, end=' ')
#             num = num // i
