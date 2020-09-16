# -*- coding: utf-8 -*-
# @Time      : 2020-03-29 20:54
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : even_odd.py
# @Software  : PyCharm


"""
A = [2,3,5,8,9,4]
"""


def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A


A = [2, 3, 5, 8, 9, 4]
print(A[2:])
print(A[2:] + A[:2])

print(even_odd(A))
