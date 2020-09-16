# -*- coding: utf-8 -*-
# @Time      : 2020-09-14 00:06
# @Author    : yuzhou_1su
# @ContactMe : www.yuzhou_1su@163.com
# @File      : singlyLinkedList.py
# @Software  : PyCharm


class ListNode:
    """链表结点定义
    """
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


class SinglyLinkedList:
    """单链表"""

    def __init__(self):
        self._head = None

    def search_list(self, element):
        """链表中查找一个元素"""

        cur = self._head
        while cur and cur.data != element:
            cur = cur.next

        # 说明这个值在此链表中
        return True


if __name__ == '__main__':
    pass

