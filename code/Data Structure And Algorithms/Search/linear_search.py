# -*- coding: utf-8 -*-
# @Time      : 2020-09-09 18:06
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : linear_search.py
# @Software  : PyCharm


def linear_search(sequence, target):
    """线性查找
    :param sequence: 待查找序列，可以无序
    :param target: 待查元素
    :return: 找到待查元素的所有；如果找不到，则返回None
    """

    for i, v in enumerate(sequence):
        if v == target:
            return i
    return None
