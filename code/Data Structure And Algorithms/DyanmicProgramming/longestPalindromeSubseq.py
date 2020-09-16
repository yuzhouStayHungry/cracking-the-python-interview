# -*- coding: utf-8 -*-
# @Time      : 2020-04-24 21:40
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : longestPalindromeSubseq.py
# @Software  : PyCharm


def longestPalindromeSubseq(s):
    """
    :type s: str
    :rtype: int
    """
    length = len(s)

    dp = [[0] * length for _ in range(length)]
    for i in range(length - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, length):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][length - 1]
