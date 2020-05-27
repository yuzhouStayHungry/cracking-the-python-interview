# -*- coding: utf-8 -*-
# @Time      : 2020-04-14 17:59
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : huawei.py
# @Software  : PyCharm

# word = "Hello"
# word = word.split(" ")
# print(word)
# print(word[-1])
# print(len(word[-1]))
#
#
# def func(s, w):
#     count = 0
#     s = s.lower()
#     for i in s:
#         if w.lower() == i:
#             count += 1
#     return count
#
# print(func("nhrwlbcc8m7c5hih9mhalw98k0322wf2jjm47kk3ntm9snfrflzzundn7d608usy049asxalzjk7izj6amcqhr8uubc04g52mcjboj2fmge2l6iarizfu4yve5o4i3srf5zgqbg82ckcotdeqp760mc9gzei5dzk5gj9x9yj05o3hle0ii64krkkp5i7blh7nbu3gu5vgi2scyn4yqx3z4vcjbyzhnqkh887izotjkg2l0mit0k14vyn", "t"))
# print("abd123ABC".lower())

# import random
#
# n = int(input())
# nums = []
# for i in range(n):
#     nums.append(input())
# print(sorted(list(set(nums))))

# print(0xAB3)
# # print(10*16**2 + 11*16 +3)
# # 
# # dic={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
# # s = input()
# # s = s[2:]
# # num = 0
# # for i in s:
# #     if i in dic:
# #         i = dic[i]
# #     num = num * 16 + int(i)
# # print(num)
# # print(s)


def countPrimes(n: int) -> int:
    count = 0
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            # print(i)
            count += 1
    return count


# countPrimes(10)
print(countPrimes(10))


# def countPrimes(self, n: int) -> int:
#     count = 0
#     for i in range(2, n):
#         for j in range(2, i // 2 + 1):
#             if i % j == 0:
#                 break
#         else:
#             # print(i)
#             count += 1
#     return count

class Solution:
    def countPrimes(self, n: int) -> int:
        # 给每个位置立一个flag，初始化为1
        isPrimes = [1] * n
        # result，输出的质数总个数的计数器，初始化为0
        res = 0
        # 循环，从最小质数i开始到n循环
        for i in range(2, n):
            # 如果这个位置的flag为1，说明数字 i  没有被比 i 小的数整除过，说明它是质数，计数器+1
            if isPrimes[i] == 1: res += 1

            # 下面这几步的思路是， i 的倍数一定不是质数，将这些数的flag设置为0
            # 设置倍数 j ，初始化与 i 相等。 因为i也是一点点加上来的，比如 i=5的时候，i 的4倍一定在 i=4 时已经设置为0过。
            j = i
            # 当 i 的 j 倍大于n的时候跳出循环
            while i * j < n:
                # 设置i 的 j 倍的flag为0
                isPrimes[i * j] = 0
                # 自增，下一个找 j+1 倍
                j += 1
        # 返回结果
        return res


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        isPrimes = [1] * n  # 立flag
        isPrimes[0] = isPrimes[1] = 0  # 设置0和1位为0
        # 下面的思路是在 2 到 根号n 的范围内，当一个数是质数，将它所有的比n小的倍数设置成0
        for i in range(2, int(n ** 0.5) + 1):
            if isPrimes[i] == 1:
                # 哇这个切片真的是pythonic
                isPrimes[i * i: n: i] = [0] * len(isPrimes[i * i: n: i])
        # 现在每个质数位的flag为1，其余的位数为0.由于我们不需要知道质数是什么只要总数，因此直接返回list里面所有1的和就行。
        return sum(isPrimes)
