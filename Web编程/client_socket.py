# -*- coding: utf-8 -*-
# @Time      : 2020-04-22 01:08
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : client_socket.py
# @Software  : PyCharm

import socket

# 创建套接字
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 要连接的服务器
client.connect(('127.0.0.1', 8888))

while True:
    # 要发送的数据
    re_data = input('客户端:')
    client.send(re_data.encode('utf8'))
    data = client.recv(1024)
    print('服务端:', data.decode('utf8'))
