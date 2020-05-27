# -*- coding: utf-8 -*-
# @Time      : 2020-02-10 23:13
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : 随机打乱列表.py
# @Software  : PyCharm

import random


def random_list1(li):
    for i in range(0, 100):
        index1 = random.randint(0, len(li) - 1)
        index2 = random.randint(0, len(li) - 1)
        li[index1], li[index2] = li[index2], li[index1]
    return li


li = [1, 2, 3, 4, 5]
test = random_list1(li)
print(test)


def random_list2(a):
    a_copy = a.copy()
    result = []
    count = len(a)
    for i in range(0, count):
        index = random.randint(0, len(a_copy) - 1)
        result.append(a_copy[index])
        del a_copy[index]
    return result


test = [1, 3, 4, 5, 6]
result = random_list2(test)
print(result)

test = [1, 2, 3, 4, 5]
random.shuffle(test)
print(test)

'''
def shuffle(self, x, random=None):
    """Shuffle list x in place, and return None.

    Optional argument random is a 0-argument function returning a
    random float in [0.0, 1.0); if it is the default None, the
    standard random.random will be used.

    """

    if random is None:
        randbelow = self._randbelow
        for i in reversed(range(1, len(x))):
            # pick an element in x[:i+1] with which to exchange x[i]
            j = randbelow(i + 1)
            x[i], x[j] = x[j], x[i]
    else:
        _int = int
        for i in reversed(range(1, len(x))):
            # pick an element in x[:i+1] with which to exchange x[i]
            j = _int(random() * (i + 1))
            x[i], x[j] = x[j], x[i]


shuffle([1, 2, 3, 4, 5])
'''
