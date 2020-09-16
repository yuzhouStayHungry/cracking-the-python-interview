# -*- coding: utf-8 -*-
# @Time      : 2020-05-12 09:39
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : threads1.py
# @Software  : PyCharm

import _thread


def child(tid):
    print("Hello from thread", tid)


def parent():
    i = 0
    while True:
        i += 1
        _thread.start_new_thread(child, (i,))

        if input() == 'q':
            break


parent()
