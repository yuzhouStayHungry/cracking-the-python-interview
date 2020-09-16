# -*- coding: utf-8 -*-
# @Time      : 2020-04-09 21:07
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : is_equals.py
# @Software  : PyCharm

def main():
    x = y = -1
    while True:
        x += 1
        y += 1
        if x is y:
            print('%d is %d' % (x, y))
        else:
            print('Attention! %d is not %d' % (x, y))
            break

    x = y = 0
    while True:
        x -= 1
        y -= 1
        if x is y:
            print('%d is %d' % (x, y))
        else:
            print('Attention! %d is not %d' % (x, y))
            break


if __name__ == '__main__':
    main()
