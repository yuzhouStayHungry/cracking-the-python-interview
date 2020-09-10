# -*- coding: utf-8 -*-
# @Time      : 2020-09-10 10:00
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : bubble_sort.py
# @Software  : PyCharm


def bubble_sort(gList):
    """冒泡排序"""
    length = len(gList)
    for i in range(length):
        for j in range(i + 1, length):
            if gList[i] > gList[j]:
                gList[i], gList[j] = gList[j], gList[i]
    return gList


if __name__ == '__main__':
    gList = [2020, 2004, 2008, 2013, 2100]
    print("-------给定序列为:", gList)
    print("-------冒泡排序后:", bubble_sort(gList))
