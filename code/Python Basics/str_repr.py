# -*- coding: utf-8 -*-
# @Time      : 2020-04-04 21:27
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : str_repr.py
# @Software  : PyCharm


class Student():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Name：" + self.name

    def __repr__(self):
        return "姓名：" + self.name


class_one = Student("Alice")
print(class_one)
print(str(class_one))
print(repr(class_one))
