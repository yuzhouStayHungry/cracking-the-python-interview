# -*- coding: utf-8 -*-
# @Time      : 2020-09-10 14:31
# @Author    : yuzhou_1su
# @ContactMe : www.yuzhou_1su@163.com
# @File      : counting_sort.py
# @Software  : PyCharm


def counting_sort(unsorted):
    """计数排序
    :param unsorted：给定一组序列
    :return: 升序序列
    """
    if unsorted is []:
        return []
    # 根据给定序列求信息
    coll_len = len(unsorted)
    coll_max = max(unsorted)
    coll_min = min(unsorted)

    # 创建计数数组
    counting_arr_length = coll_max + 1 - coll_min
    counting_arr = [0] * counting_arr_length

    # 计数操作
    for number in unsorted:
        counting_arr[number - coll_min] += 1

    # 将每个位置与它的前一个相加。counting_arr[i]统计出多少个
    # element <= i的元素
    for i in range(1, counting_arr_length):
        counting_arr[i] = counting_arr[i] + counting_arr[i - 1]

    # 创建保存升序结果的数组
    ordered = [0] * coll_len
    for i in reversed(range(0, coll_len)):
        ordered[counting_arr[unsorted[i] - coll_min] - 1] = unsorted[i]
        counting_arr[unsorted[i] - coll_min] -= 1

    return ordered


if __name__ == '__main__':
    gList = [5, 4, 2, 1, 3, 6]
    print("-----yuzhou1su：", gList)
    print("-----计数排序后:", counting_sort(gList))
