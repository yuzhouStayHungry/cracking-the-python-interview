# -*- coding: utf-8 -*-
# @Time      : 2020-09-10 09:41
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : selection_sort.py
# @Software  : PyCharm


def selection_sort(gList):
    """选择排序
    :param gList: 给定的一组序列
    :return: 返回排好序的序列
    """
    length = len(gList)
    for i in range(length - 1):
        flag = i
        for j in range(i + 1, length):
            if gList[flag] > gList[j]:
                flag = j
        # 如果最小值的索引与最小值相对应，则无需再次交换
        if flag != i:
            gList[flag], gList[i] = gList[i], gList[flag]

    return gList


if __name__ == '__main__':
    gList = [2020, 2004, 2008, 1001, 2100]
    print("-------给定序列为:", gList)
    print("-------选择排序后:", selection_sort(gList))
