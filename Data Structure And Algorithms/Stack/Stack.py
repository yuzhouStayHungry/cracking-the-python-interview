# -*- coding: utf-8 -*-
# @Time      : 2020-01-08 10:59
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : Stack.py
# @Software  : PyCharm

"""
Stack is a special kind of data structure that follows Last-In-First-Out(LIFO) strategy.
this means that the element that is added to stack last will be the first to be removed.
"""


class Stack(object):
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


def main():
    mystack = Stack()  # create a stack
    print("栈是否为空：", mystack.is_empty())
    mystack.push(3)
    mystack.push(1)
    mystack.push(6)
    mystack.push(1)
    mystack.push(10)
    mystack.push(10)
    print("栈是否为空: ", mystack.is_empty())
    print("栈中元素: ", mystack.all())
    print("栈中元素数量: ", len(mystack))
    print("栈顶元素: ", mystack.top())
    print("出栈：", mystack.pop())
    print("出栈：", mystack.pop())
    print("栈中元素:", mystack.all())


if __name__ == '__main__':
    main()
