# -*- coding: utf-8 -*-
# @Time      : 2020-04-05 19:19
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : leetcode_242.py
# @Software  : PyCharm

'''
LeetCode第242题：给定两个字符串s和t，编写一个函数来判断t是否是s的字母异位词。

说明：你可以假设字符串只包含小写字母。
输入: s = "anagram", t = "nagaram"

输出: true

'''


def isAnagram(s: str, t: str):
    if len(s) != len(t):
        return False

    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for j in t:
        if j not in d or d[j] <= 0:
            return False
        d[j] -= 1

    for v in d:
        if d[v] != 0:
            return False
    return True


s = "anagram"
t = "nagaram"

s2 = "atc"
t2 = "rat"
print(isAnagram(s, t))
print(isAnagram(s2, t2))
