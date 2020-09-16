# -*- coding: utf-8 -*-
# @Time      : 2020-01-06 21:30
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : twostrs_isPermutation.py
# @Software  : PyCharm

class Solution():
    """
   @param: A: a string
    @param: B: a string
    @return: a boolean
    """

    def isPermutation1(self, str1, str2):

        if len(str1) != len(str2):
            return False

        hash_mapA = dict()
        hash_mapB = dict()

        for i, _ in enumerate(str1):
            hash_mapA[str1[i]] = str1[i]
            hash_mapB[str2[i]] = str2[i]

        if hash_mapA != hash_mapB:
            return False

        return True

    def isPermutation2(self, A, B):
        list1 = [i for i in A]
        list2 = [j for j in B]
        list1.sort()
        list2.sort()
        if list1 == list2:
            return True
        else:
            return False


str1 = "cabcd"
str2 = "bcdac"
str3 = "abcae"
A = Solution()
print(A.isPermutation1(str1, str2))
print(A.isPermutation1(str1, str3))

print(A.isPermutation2(str1, str2))
print(A.isPermutation1(str2, str3))
