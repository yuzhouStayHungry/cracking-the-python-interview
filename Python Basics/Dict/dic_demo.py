# -*- coding: utf-8 -*-
# @Time      : 2020-04-02 20:03
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : dic_demo.py
# @Software  : PyCharm

dic = {"name": "snails", "age": 18}

print(dic)

# del dic["name"]
dic.pop("name")

print(dic)

list_t = [1, 2, 3, 4, 5]


def func(x):
    return x ** 2


result = map(func, list_t)
result = [i for i in result if i > 10]
print(result)

a = (1,)
b = (1)
c = ("1")
print("a:{}, b:{}, c:{}".format(type(a), type(b), type(c)))
