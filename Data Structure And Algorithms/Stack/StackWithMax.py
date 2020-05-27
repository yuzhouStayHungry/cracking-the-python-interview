# -*- coding: utf-8 -*-
# @Time      : 2020-01-09 11:37
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : StackWithMax.py
# @Software  : PyCharm

import sys

sys.path.append('/Users/yuzhou_1su/PycharmProjects/cracking-the-python-interview/Stack')
from DataStructureAndAlgorithm.Stack import Stack


class StackWithMax(Stack):
    """
    具有push()、pop()和带有max()方法，其复杂度为O(1).
    """

    def __init__(self):
        self.stackData = Stack()
        self.stackMax = Stack()

    def push(self, newNum):
        if self.stackMax.is_empty():
            self.stackMax.push(newNum)
        elif newNum >= self.gex_max():
            self.stackMax.push(newNum)
        self.stackData.push(newNum)

    def pop(self):
        if self.stackData.is_empty():
            raise Empty('stackData is empty.')
        value = self.stackData.pop()
        if value == self.gex_max():
            self.stackMax.pop()
        return value

    def gex_max(self):
        if self.stackMax.is_empty():
            raise Empty('stackMax is empty.')
        return self.stackMax.top()


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


def main():
    mystack2 = StackWithMax()
    mystack2.push(3)
    mystack2.push(1)
    mystack2.push(6)
    mystack2.push(1)
    mystack2.push(10)
    mystack2.push(10)
    print("mystack2中stackData的所有元素", mystack2.stackData.all())
    print("mystack2中stackData的栈顶元素:", mystack2.stackData.top())
    print("mystack2中stackMax的所有元素", mystack2.stackMax.all())

    print("max：", mystack2.gex_max())
    mystack2.pop()
    mystack2.pop()
    mystack2.pop()
    print("mystack2中stackData的所有元素", mystack2.stackData.all())
    print("max: ", mystack2.gex_max())
    mystack2.pop()
    print("mystack2中stackData的所有元素", mystack2.stackData.all())
    print("max:", mystack2.gex_max())
    mystack2.pop()
    print("mystack2中stackData的所有元素", mystack2.stackData.all())


if __name__ == '__main__':
    main()
