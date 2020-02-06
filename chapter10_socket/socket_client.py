# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-10 17:58:31
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-10 19:58:51
 * @Description: None
'''
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
while True:
    re_data = input()
    client.send(re_data.encode("utf8"))
    # data = client.recv(1024) 
    # print(data.decode("utf8"))

# client.send('wanghao'.encode('utf8'))
# client.close()