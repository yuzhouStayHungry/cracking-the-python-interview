# -*- coding: utf-8 -*-
# @Time      : 2020-09-10 15:59
# @Author    : yuzhou_1su
# @ContactMe : www.yuzhou_1su@163.com
# @File      : radix_sort.py
# @Software  : PyCharm


def radix_sort(unsorted):
    radix = 10
    max_len = False
    tmp, placement = -1, 1
    while not max_len:
        max_len = True
        buckets = [list() for _ in range(radix)]
        for i in unsorted:
            tmp = int(i / placement)
            buckets[tmp % radix].append(i)
            if max_len and tmp > 0:
                max_len = False
        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                unsorted[a] = i
                a += 1
        # move to next digit
        placement *= radix
    return unsorted


if __name__ == '__main__':
    gList = [5, 4, 2, 1, 3, 6]
    print("-----yuzhou1su：", gList)
    print("-----基数排序后:", radix_sort(gList))
