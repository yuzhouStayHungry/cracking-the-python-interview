# -*- coding: utf-8 -*-
# @Time      : 2020-04-22 01:05
# @Author    : yuzhou_1su
# @ContactMe : https://blog.csdn.net/yuzhou_1shu
# @File      : server_socket.py
# @Software  : PyCharm

import socket

# 创建套接字
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP和端口,元组存储地址和端口
server.bind(('0.0.0.0', 8888))

# 服务端监听
server.listen()

# accept接受到用户的请求
sock, addr = server.accept()

while True:
    # 接受从客户端发送的数据,一次获取1k的数据
    data = sock.recv(1024)

    # 打印接收的数据
    print('客户端:', data.decode('utf8'))
    re_data = input('服务器:')

    sock.send(re_data.encode('utf8'))
