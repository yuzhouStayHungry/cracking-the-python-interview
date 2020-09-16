# -*- coding: utf-8 -*-
# @Time      : 2020-04-04 16:52
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : TwilightBus.py
# @Software  : PyCharm


class TwilightBus():
    """乘客消失的校车"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            # 这个赋值语句把 self.passengers 变成 passengers 的别 名，而后者是传给 __init__ 方法的实参
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


class TwilightBus2():
    """乘客消失的校车"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            #  校车自己维护乘客列表
            #  创建 passengers 列表的副本;如果不是列表，就把它转换成列表。
            #  在内部像这样处理乘客列表，就不会影响初始化校车时传入的参数了。
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def main():
    basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
    bus = TwilightBus(basketball_team)
    # bus.drop('Tina')
    # bus.drop('Sue')

    # print(bus.passengers)
    # print(basketball_team)

    bus2 = TwilightBus2(basketball_team)
    bus2.drop('Tina')
    bus2.drop('Sue')

    print(bus2.passengers)
    print(basketball_team)


if __name__ == '__main__':
    main()
