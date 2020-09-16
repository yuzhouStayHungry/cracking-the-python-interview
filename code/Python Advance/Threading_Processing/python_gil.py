# -*- coding: utf-8 -*-
# @Time      : 2020-04-15 08:18
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : python_gil.py
# @Software  : PyCharm

# GIL- global interpreter lock (cpython)
# Python中的一个线程对应c语言中的一个线程，
# GIL使得一个线程运行在一个CPU上执行字节码
# 无法将多个线程映射到多个CPU上执行

# import dis
#
#
# def add(a):
#     a += 1
#     return a
#
#
# print(dis.dis(add))

total = 0


def add():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


# GIL 会根据执行的字节码行数以及时间片释放GIL，
# 遇到IO操作，也会得到释放
# import threading
# thread1 = threading.Thread(target=add)
# thread2 = threading.Thread(target=desc)
# thread1.start()
# thread2.start()
# 
# thread1.join()
# thread2.join()
# 
# print(total)
import multiprocessing

mp1 = multiprocessing.Process(target=add)
mp2 = multiprocessing.Process(target=desc)

mp1.start()
mp2.start()

mp1.join()
mp2.join()
print(total)
