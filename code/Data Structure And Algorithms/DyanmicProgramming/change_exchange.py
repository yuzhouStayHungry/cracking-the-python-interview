# -*- coding: utf-8 -*-
# @Time      : 2020-04-24 19:34
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : change_exchange.py
# @Software  : PyCharm


def coinChangeRecursive(coins, amount):
    def dp(n):

        # base case
        if n == 0:
            return 0
        if n < 0:
            return -1
        # 求最小值，所以初始化为正无穷
        res = float('INF')
        for coin in coins:
            sub_problem = dp(n - coin)
            # 子问题无解，跳过
            if sub_problem == -1:
                continue
            res = min(res, 1 + sub_problem)
        return res if res != float('INF') else -1

    return dp(amount)


def coinChangeRecursiveWithMemo(coins, amount):
    # 备忘录
    memo = dict()

    def dp(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('INF')
        for coin in coins:
            sub_problem = dp(n - coin)
            if sub_problem == -1:
                continue
            res = min(res, 1 + sub_problem)

        # 记录备忘录
        memo[n] = res if res != float('INF') else -1
        return memo[n]

    return dp(amount)


# dp数组的迭代解法
def coinChangeIterative(coins, amount):
    # 定义一个数组长度为amount+1的数组，值也为amount+1
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if i >= coins[j]:
                dp[i] = min(dp[i], 1 + dp[i - coins[j]])
    return -1 if dp[-1] == amount + 1 else dp[-1]


#
# def coinChange(coins, amount):
#     dp = [float('inf')] * (amount + 1)
#     dp[0] = 0
#
#     for coin in coins:
#         for x in range(coin, amount + 1):
#             dp[x] = min(dp[x], dp[x - coin] + 1)
#     return dp[amount] if dp[amount] != float('inf') else -1


def coinChange(coins, amount) -> int:
    dp = [float('INF')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if i >= coins[j]:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    return dp[-1] if dp[-1] != float('INF') else -1


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [float('INF')] * (amount + 1)
#         dp[0] = 0
#
#         for i in range(1, amount + 1):
#             for j in range(len(coins)):
#                 if i >= coins[j]:
#                     dp[i] = min(dp[i], dp[i - coins[j]] + 1)
#         return dp[amount] if dp[amount] != float('INF') else -1


# res = coinChangeRecursive([1, 2, 5], 11)
# print(res)
#
# print(coinChangeRecursiveWithMemo([1, 2, 5], 11))
# print(coinChangeIterative([1, 2, 5], 11))
print(coinChange([1, 2, 5], 11))
