# -*- coding: utf-8 -*-
# @Time      : 2020-04-04 12:40
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : demo.py
# @Software  : PyCharm


class Demo:
    def __init__(self):
        print('Demo id: %d' % id(self))


def main():
    x = Demo()
    # y = Demo() * 10

    alex = {'nickname': 'yu', 'born': 1996}
    bob = {'nickname': 'yu', 'born': 1996}
    print(alex == bob)  # ==运算符比较两个对象的值（对象中保存的数据）
    print(alex is bob)  # is比较对象的标识

    l1 = [3, [55, 44], (7, 8, 9)]
    l2 = list(l1)
    print("l1:", l1)
    print("l2:", l2)
    print(l1 == l2)
    print(l1 is l2)

    l3 = l1[:]
    print("l3:", l3)
    print(l1 is l3)

    l1.append(100)
    l1[1].remove(55)
    print("l1:", l1)
    print("l2:", l2)

    l2[1] += [33, 22]
    l2[2] += (10, 11)
    print("l1:", l1)
    print("l2:", l2)

    a = [10, 20]
    b = [a, 30]
    a.append(b)
    print(a)

    from copy import deepcopy
    c = deepcopy(a)
    print(c)


if __name__ == '__main__':
    main()
