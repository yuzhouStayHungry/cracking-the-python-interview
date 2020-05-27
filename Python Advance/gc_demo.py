# -*- coding: utf-8 -*-
# @Time      : 2020-04-26 08:27
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : gc_demo.py
# @Software  : PyCharm

def extend_list(val, l=[]):
    print(l, id(l))
    l.append(val)
    print(l, id(l))
    return l


list1 = extend_list(10)
print(list1)

list2 = extend_list(123, [])
print(list2)

list3 = extend_list('s')

print(list3)


class ClassGc():
    def __init__(self):
        print('对象产生: {0}'.format(id(self)))

    def __del__(self):
        print('对象回收: {0}'.format(id(self))


def loop():
    while True:
        c1 = ClassGc()


def loop2():
    l = []
    while True:
        c1 = ClassGc()
        l.append(c1)
        print(len(l))


if __name__ == '__main__':
    loop()
    loop2()
