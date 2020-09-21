# -*- coding: utf-8 -*-
# @Time      : 2020-09-10 12:30
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : quick_sort.py
# @Software  : PyCharm


def quick_sort(gList, left=0, right=None) -> list:
    """快速排序
    :param gList: 给定一组序列
    :param left:
    :param right:
    :return: 升序排序后的序列
    """
    if right is None:
        right = len(gList) - 1

    if left > right:
        return gList

    key = gList[left]
    low = left
    high = right

    while left < right:
        while left < right and gList[right] >= key:
            right -= 1
        gList[left] = gList[right]

        while left < right and gList[left] <= key:
            left += 1
        gList[right] = gList[left]
    gList[right] = key
    quick_sort(gList, low, left - 1)
    quick_sort(gList, left + 1, high)
    return gList


def quicksort(array):
    less = []
    greater = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for x in array:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    gList = [3, 5, 2, 4, 1, 6, 7]
    print("----排序前:", gList)
    print("----快速排序后: ", quick_sort(gList))

    print(quicksort(gList))
