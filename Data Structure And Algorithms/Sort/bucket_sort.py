# -*- coding: utf-8 -*-
# @Time      : 2020-09-10 15:30
# @Author    : yuzhou_1su
# @ContactMe : www.yuzhou_1su@163.com
# @File      : bucket_sort.py
# @Software  : PyCharm
import math


def insertion_sort(collection):
    for i in range(1, len(collection)):
        temp = collection[i]
        index = i
        while index > 0 and temp < collection[index - 1]:
            collection[index] = collection[index - 1]
            index -= 1
        collection[index] = temp


def bucket_sort(collection):
    code = hashing(collection)
    buckets = [list() for _ in range(code[1])]
    for i in collection:
        x = rehashing(i, code)
        buck = buckets[x]
        buck.append(i)

    for bucket in buckets:
        insertion_sort(bucket)

    ndx = 0
    for buc in range(len(buckets)):
        for val in buckets[buc]:
            collection[ndx] = val
            ndx += 1
    return collection


def hashing(collection):
    m = collection[0]
    for i in range(1, len(collection)):
        if m < collection[i]:
            m = collection[i]
    result = [m, int(math.sqrt(len(collection)))]
    return result


def rehashing(i, code):
    return int(i / code[0] * (code[1] - 1))


if __name__ == '__main__':
    gList = [5, 4, 2, 1, 3, 6]
    print("-----yuzhou1su：", gList)
    print("-----桶排序后:", bucket_sort(gList))
