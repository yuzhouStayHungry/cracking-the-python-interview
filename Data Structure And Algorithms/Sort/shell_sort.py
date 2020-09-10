# -*- coding: utf-8 -*-
# @Time      : 2020-09-10 12:59
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : shell_sort.py
# @Software  : PyCharm


def shell_sort(gList) -> list:
    """希尔排序"""
    length = len(gList)
    step = 2
    group = length // step
    while group > 0:
        for startPos in range(group):
            gap_insertion_sort(gList, startPos, group)
        group = group // 2
    return gList


def gap_insertion_sort(gList, start, gap):
    for i in range(start + gap, len(gList), gap):
        curr_value = gList[i]
        pos = i

        while pos >= gap and gList[pos - gap] > curr_value:
            gList[pos] = gList[pos - gap]
            pos = pos - gap
        gList[pos] = curr_value


if __name__ == '__main__':
    gList = [5, 4, 2, 1, 7, 3, 6]
    print("-----yuzhou1su-----", gList)
    print("-----希尔排序后:", shell_sort(gList))
