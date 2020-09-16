# -*- coding: utf-8 -*-
# @Time      : 2020-05-12 10:19
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : threads2.py
# @Software  : PyCharm

from _thread import start_new_thread
import time


def sing():
    for i in range(3):
        print("I'm singing 难忘今宵")
        time.sleep(2)


def dance():
    for i in range(3):
        print("I'm dancing")
        time.sleep(2)


def main():
    start_new_thread(sing, ())
    start_new_thread(dance, ())
    time.sleep(6)
    print('Main thread exiting...')


if __name__ == '__main__':
    main()
