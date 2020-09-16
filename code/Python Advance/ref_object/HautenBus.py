# -*- coding: utf-8 -*-
# @Time      : 2020-04-04 16:38
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : HautenBus.py
# @Software  : PyCharm


class HauntedBus:

    def __init__(self, passengers=[]):
        self.passengers = passengers  # 别名；不传参，后者又是默认列表的别名

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def main():
    bus1 = HauntedBus(['Alice', 'Alex', 'Bob'])
    print(bus1.passengers)
    bus1.pick('Bill')
    bus1.drop('Alice')
    print(bus1.passengers)

    bus2 = HauntedBus()
    bus2.pick('Wade')
    print(bus2.passengers)

    bus3 = HauntedBus()
    print(bus3.passengers)
    bus3.pick('Dave')

    print(bus2.passengers)

    print(bus2.passengers is bus3.passengers)

    print(bus1.passengers)

    print(dir(HauntedBus.__init__))
    print(HauntedBus.__init__.__defaults__)
    print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)


if __name__ == '__main__':
    main()
