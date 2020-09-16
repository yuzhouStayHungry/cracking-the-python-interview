# -*- coding: utf-8 -*-
# @Time      : 2020-04-01 11:54
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : fibnacci_problem.py
# @Software  : PyCharm

from datetime import datetime
from collections import defaultdict


def fib_test(k):
    if k in [1, 2]:
        return 1
    return fib_test(k - 1) + fib_test(k - 2)


memo = defaultdict(int)


def fib_test_with_memo(k):
    if k in [1, 2]:
        return 1
    global memo
    if k in memo:
        result = memo[k]
    else:
        result = fib_test_with_memo(k - 1) + fib_test_with_memo(k - 2)
        memo[k] = result
    return result


def fib_no_rec1(k):
    assert k > 0, "k必须大于0"
    if k in [1, 2]:
        return 1

    k_1 = 1
    k_2 = 1
    for i in range(3, k + 1):
        tmp = k_1
        k_1 = k_1 + k_2
        k_2 = tmp
    return k_1


def fib_no_rec2(n):
    f = [0, 1, 1]
    if n > 2:
        for i in range(n - 2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]


if __name__ == "__main__":
    print(fib_test(7))
    print(fib_no_rec1(7))
    print(fib_no_rec2(7))

    print(fib_test(20))
    print(fib_no_rec2(20))

    start_time = datetime.now()
    print(fib_no_rec2(50))
    print("递归耗时: {}".format(datetime.now() - start_time))

    start_time = datetime.now()
    print(fib_test_with_memo(50))
    print("递归耗时: {}".format(datetime.now() - start_time))
