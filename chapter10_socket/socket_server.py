# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-10 17:58:38
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-10 19:58:28
 * @Description: None
'''
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP, UDP socket.SOCK_DGRAM
server.bind(('0.0.0.0', 8000))
server.listen()

def handle_sock(sock, addr):
    while True:
        re_data = input()
        sock.send(re_data.encode("utf-8"))
        data = sock.recv(1024)
        print(data.decode("utf-8"))

while True:
    sock, addr = server.accept()

    # 用线程去处理新接手的连接
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

    # 获取从客户端发送的数据
    data = sock.recv(1024) # 一次接收1024（1k）字节的数据
    print(data.decode("utf8"))
    # re_data = input()
    # sock.send(re_data.encode("utf8"))
    # sock.close()
    # server.close()