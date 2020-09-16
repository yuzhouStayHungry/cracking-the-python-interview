# -*- coding: utf-8 -*-
# @Time      : 2020-01-07 20:44
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : class_attr_and_instance_attr.py
# @Software  : PyCharm


class A:
    x = 1


class B(A):
    pass


class C(A):
    pass


print([A.x, B.x, C.x])

B.x = 2
print([A.x, B.x, C.x])

A.x = 3
print([A.x, B.x, C.x])

a = A()
print([a.x, A.x])

a.x += 1
print([a.x, A.x])


class SomeClass:
    some_var = 15
    some_list = [5]
    another_list = [5]

    def __init__(self, x):
        self.some_var = x + 1
        self.some_list = self.some_list + [x]
        self.another_list += [x]


some_obj = SomeClass(420)
print(some_obj.some_list)
print(some_obj.another_list)

another_obj = SomeClass(111)
print(another_obj.some_list)
print(another_obj.another_list)

print(another_obj.another_list is SomeClass.another_list)
print(another_obj.another_list is some_obj.another_list)
