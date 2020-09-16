# -*- coding: utf-8 -*-
# @Time      : 2020-04-15 08:51
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : single_threaded.py
# @Software  : PyCharm

import time
from threading import Thread

COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


start_time = time.time()
countdown(COUNT)
end_time = time.time()

print('Time taken in seconds:', end_time - start_time)
