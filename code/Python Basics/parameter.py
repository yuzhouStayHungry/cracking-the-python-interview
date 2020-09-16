# -*- coding: utf-8 -*-
# @Time      : 2020-01-07 15:57
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : parameter.py
# @Software  : PyCharm

array = [1, 8, 15]
g = (x for x in array if array.count(x) > 0)
array = [2, 8, 22]

print(list(g))

a = 256
b = 256
print(a is b)

c = 257
d = 257
print(c is d)

funcs = []
results = []
for x in range(7):
    def some_func():
        return x


    funcs.append(some_func)
    results.append(some_func())

funcs_results = [func() for func in funcs]
print(results)
print(funcs_results)

powers_of_x = [lambda x: x ** i for i in range(10)]
[f(2) for f in powers_of_x]

funcs = []
for x in range(7):
    def some_func(x=x):
        return x


    funcs.append(some_func)
funcs_results = [func() for func in funcs]
print(funcs_results)
