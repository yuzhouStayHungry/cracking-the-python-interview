# -*- coding: utf-8 -*-
# @Time      : 2020-04-23 21:28
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : Circle_back_to_start.py
# @Software  : PyCharm


'''
一个环上有10个点，编号为0-9，从0点出发，每步可以顺时针到下一个点，也可以逆时针到上一个点，
求：经过n步又回到0点有多少种不同的走法?

思考：
    0步 就在原点。共1种走法
    1步 0->1 、0->9，回不到原点。共0种走法
    2步 0->1->2 、0->9->8 回不到原点；0->1->0、 0->9->0 共2种走法
    3步 0->1->2->3、0->1->2->1、0-1-0-1

    0点可以从右面回来，也可以从左面回来，即先到达0旁边的一个点

    d(k,j) = d(k-1, j-1) + d(k-1, j+1)
    表示点j走k步回到原点0的方法，因此可以转化为他相邻的点经过k-1步回到原点的问题

    由于是环问题，j-1、j+1会超出0~n-1的范围。修改递推式:
    d(k, j) = d(k-1, (j-1+n)%n) + d(k-1, (j+1)%n)
'''


# n 代表点的个数，s代表步数
def get_steps(n, s):
    if n == 0:
        return 1
    if n == 2:
        if n % 2 == 0:
            return 1
        else:
            return 0

    dp = [[0 for i in range(100)] for j in range(100)]

    dp[0][0] = 1
    for i in range(n):
        dp[0][i] = 0
    for s in range(s):
        for i in range(n):
            dp[s][i] = dp[s - 1][(i - 1 + n) % n] + dp[i - 1][(i + 1) % n]
    return dp[s][0]


steps = get_steps(9, 2)
print(steps)
