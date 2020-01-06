# -*- coding: utf-8 -*-
# @Time      : 2020-01-06 20:42
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : string_isUnique.py
# @Software  : PyCharm

'''
Description:
    1. Determine if all characters of a string are unique.
    判断一个字符串所有的字符是否都是唯一的。
'''


class Solution:
    """

    @:param str: A String
    @:return: a boolean

    """

    def isUnique_by_count(self, string):

        li = list(string)
        for i in range(len(li)):
            if string.count(li[i]) != 1:
                return False
        return True

    def isUnique(self, string):

        hash_map = dict()

        for i, j in enumerate(string):
            if j in hash_map:
                return False
            hash_map[j] = i
        return True


str1 = "abcd"
str2 = "ABcdBea"
A = Solution()
print(A.isUnique(str1))
print(A.isUnique_by_count(str1))

print(A.isUnique(str2))
print(A.isUnique_by_count(str2))
