# -*- coding: utf-8 -*-
# @Time      : 2020-09-10 14:13
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : heap_sort.py
# @Software  : PyCharm


def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    """堆排序"""
    length = len(unsorted)
    for i in range(length // 2 - 1, -1, -1):
        heapify(unsorted, i, length)
    for i in range(length - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted


if __name__ == '__main__':
    gList = [5, 4, 2, 1, 7, 3, 6]
    print("-----yuzhou1su-----", gList)
    print("-----堆排序后:", heap_sort(gList))
