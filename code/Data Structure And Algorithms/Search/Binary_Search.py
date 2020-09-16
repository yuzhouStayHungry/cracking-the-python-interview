# -*- coding: utf-8 -*-
# @Time      : 2020-04-11 23:28
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : Binary_Search.py
# @Software  : PyCharm


def binary_search1(arr, item):
    """
    二分查找的非递归实现1

    :param arr: 有序数组
    :param item: 待查元素
    :return: 找到待查元素的所有；如果找不到，则返回None
    """
    low = 0
    high = len(arr) - 1  # 注意此处，high索引能取到

    while low <= high:  # 条件是low<=high，区间中没有元素时结束
        mid = (low + high) // 2
        curr_item = arr[mid]

        if curr_item == item:
            return mid
        elif item < curr_item:
            high = mid - 1  # high = mid - 1
        else:
            low = mid + 1
    return None


def binary_search2(arr, item):
    """
    左边界为n的二分查找

    :param arr: 给定一个有序数组
    :param item: 待查找的元素
    :return: 找到待查元素的所有；如果找不到，则返回None
    """

    low = 0
    high = len(arr)  # 此处 high的索引不能取到
    while low < high:  # 条件是low<high,区间中有一个元素时也结束
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid
        elif item < arr[mid]:
            high = mid  # high = mid
        else:
            low = mid + 1

    return None


def binary_search3_by_recursion(arr, item, low=0, high=None):
    """
    二分查找的递归实现
    :param arr: 有序数组
    :param item: 待查元素
    :param low: 左边界
    :param high: 右边界
    :return: 找到待查元素的所有；如果找不到，则返回None
    """
    if high is None:
        high = len(arr) - 1

    # 递归终止条件
    if low > high:
        return None
    mid = low + (high - low) // 2  # 防止溢出
    if arr[mid] == item:
        return mid
    elif arr[mid] > item:
        return binary_search3_by_recursion(arr, item, low, mid - 1)
    else:
        return binary_search3_by_recursion(arr, item, mid + 1, high)


if __name__ == '__main__':
    test_arr = [0, 2, 9, 28, 61]
    print("-----------yuzhou1su--------------")
    print(binary_search1(test_arr, 2))
    print(binary_search1(test_arr, 8))
    print(binary_search1(test_arr, 61))

    print("-----------yuzhou1su--------------")
    print(binary_search2(test_arr, 2))
    print(binary_search2(test_arr, 8))
    print(binary_search2(test_arr, 61))

    print("-----------yuzhou1su--------------")
    low = 0
    high = len(test_arr) - 1
    print(binary_search3_by_recursion(test_arr, 2))
    print(binary_search3_by_recursion(test_arr, 8))
    print(binary_search3_by_recursion(test_arr, 61))
