# -*- coding: utf-8 -*-
# @Time      : 2020-04-05 18:25
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : string_reverse.py
# @Software  : PyCharm

from collections import deque
from functools import reduce


# 利用Python翻转字符串的几种解法

# 1. 双指针法
def string_reverse1(string):
    s_l = list(string)
    begin = 0
    end = len(s_l) - 1
    while begin < end:
        s_l[begin], s_l[end] = s_l[end], s_l[begin]
        begin += 1
        end -= 1
    return ''.join(s_l)


# 2. 递归法
def string_reverse2(string):
    if string == "":
        return string
    else:
        return string_reverse2(string[1:]) + string[0]


# 3. python内置切片
def string_reverse3(string):
    return string[::-1]


# 4. 转化列表然后用内置reverse函数
def string_reverse4(string):
    s_l = list(string)
    s_l.reverse()
    return ''.join(s_l)


# 一行代码，列表生成式
def string_reverse5(string):
    return ''.join(string[i] for i in range(len(string) - 1, -1, -1))


# 双端队列
def string_reverse6(string):
    d = deque()
    d.extendleft(string)
    return ''.join(d)


# 使用reduce
def string_reverse7(string):
    return reduce(lambda x, y: y + x, string)


# 使用栈
def string_reverse8(string):
    l = list(string)  # 模拟全部入栈
    result = ""
    while len(l) > 0:
        result += l.pop()  # 模拟出栈
    return result


# 暴力：for循环
def string_reverse(string):
    result = ""
    max_index = len(string) - 1
    for index, value in enumerate(string):
        result += string[max_index - index]
    return result


def main():
    # test = "algorithm"
    test = "I love 我家"

    print("1: ", string_reverse1(test))
    print("2: ", string_reverse2(test))
    print("3: ", string_reverse3(test))
    print("4: ", string_reverse4(test))
    print("5: ", string_reverse5(test))
    print("6: ", string_reverse6(test))
    print("7: ", string_reverse7(test))
    print("8: ", string_reverse8(test))
    print("9: ", string_reverse(test))


if __name__ == '__main__':
    main()
