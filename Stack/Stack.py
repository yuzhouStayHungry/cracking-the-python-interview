# -*- coding: utf-8 -*-
# @Time      : 2020-01-08 10:59
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : Stack.py
# @Software  : PyCharm

"""
设计一个栈
"""


class ArrayStack(object):
    _slots__ = '_items'

    def __init__(self):
        self._items = []

    def __len__(self):
        """
        Return the number of element in the stack
        :return: length
        """
        return len(self._items)

    def is_empty(self):
        """
        Return True if stack is empty.
        :return:
        """
        return len(self._items) == 0

    def push(self, e):
        """
        Add element e to the top of the stack.
        :param e:
        :return:
        """
        self._items.append(e)

    def pop(self):
        """
        Remove and return the element from the top of the stack.

        Raise Empty exception if the stack is empty.
        :return:
        """
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._items.pop()

    def top(self):
        """
        Return (but do not to remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        :return:
        """
        if self.is_empty():
            raise Empty('Stack is empty')

        return self._items[-1]

    def all(self):
        return self._items[:]


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class StackWithMax(ArrayStack):
    """
    具有push()、pop()和带有max()方法，其复杂度为O(1).
    """

    def __init__(self):
        self.stackData = ArrayStack()
        self.stackMax = ArrayStack()

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


def main():
    # mystack = ArrayStack()
    # print(mystack.is_empty())
    # mystack.push(1)
    # mystack.push(2)
    # print(mystack.all())
    # print(mystack.top())
    # print(mystack.pop())
    # print(mystack.all())

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
    print(mystack2.gex_max())


if __name__ == '__main__':
    main()
