# -*- coding: utf-8 -*-
# @Time      : 2020-04-15 08:54
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : muti_threaded.py
# @Software  : PyCharm

# import time
# # from threading import Thread
# #
# # COUNT = 50000000
# #
# # def countdown(n):
# #     while n > 0:
# #         n -= 1
# #
# #
# # t1 = Thread(target=countdown, args=(COUNT//2,))
# # t2 = Thread(target=countdown, args=(COUNT//2,))
# #
# # start_time = time.time()
# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()
# # end_time = time.time()
# #
# # print('Time cost in second: ', end_time - start_time)

from multiprocessing import Pool
import time

COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    pool = Pool(processes=2)
    start_time = time.time()
    r1 = pool.apply_async(countdown, [COUNT // 2])
    r2 = pool.apply_async(countdown, [COUNT // 2])
    pool.close()
    pool.join()
    end_time = time.time()
    print('Time taken in second:', end_time - start_time)
