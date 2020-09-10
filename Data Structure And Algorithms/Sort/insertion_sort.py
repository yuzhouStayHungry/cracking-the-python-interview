# -*- coding: utf-8 -*-
# @Time      : 2020-09-10 10:00
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : insertion_sort.py
# @Software  : PyCharm


def insertion_sort(gList):
    """插入排序"""
    length = len(gList)
    for i in range(1, length):
        key = gList[i]  # 当前的待插入的值
        j = i - 1  # 前一个值
        while j >= 0:
            if gList[j] > key:
                gList[j + 1] = gList[j]  # 插入的动作
                gList[j] = key  # 插入完毕
            j -= 1
    return gList


if __name__ == '__main__':
    gList = [2020, 2004, 2008, 2013, 2100]
    print("-------给定序列为:", gList)
    print("-------插入排序后:", insertion_sort(gList))
