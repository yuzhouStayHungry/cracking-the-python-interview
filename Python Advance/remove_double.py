# -*- coding: utf-8 -*-
# @Time      : 2020-04-01 20:16
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : remove_double.py
# @Software  : PyCharm


def remove_double(li):
    if len(li) == 0:
        return 0
    i = 0
    for j in range(1, len(li)):
        if li[j] != li[i]:
            i += 1
            li[i] = li[j]
        print(li)
    return i + 1


def remove_duplicate(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.remove(nums[i])
        else:
            i = i + 1
    return len(nums)


list_test = [0, 0, 1, 1, 1, 2]
# print(remove_double(list_test))

print(remove_duplicate(list_test))
