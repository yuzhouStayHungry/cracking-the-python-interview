# -*- coding: utf-8 -*-
# @Time      : 2020-09-10 12:08
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : merge_sort.py
# @Software  : PyCharm


def merge_sort(gList: list) -> list:
    """归并排序
    :param gList: 给定序列
    :return: 升序排列后的集合
    """

    def merge(left: list, right: list) -> list:
        """merge left and right
        :param left: left list
        :param right: right list
        :return: merge reslut
        """
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    if len(gList) <= 1:
        return gList
    num = len(gList) // 2
    left = merge_sort(gList[:num])
    right = merge_sort(gList[num:])
    return merge(left, right)


if __name__ == '__main__':
    gList = [3, 5, 2, 4, 1]
    print("----排序前:", gList)
    print("----归并排序后: ", merge_sort(gList))
