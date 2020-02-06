# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-11 09:46:54
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-11 10:13:35
 * @Description: None
'''
# epoll 并不代表比 select 好
# 并发高的情况下，连接活跃度不是很高，epoll比select好
# 并发性不高，同时连接很活跃，select比epoll好

import socket
from urllib.parse import urlparse

# 使用非组赛IO
def get_url(url):
    # 通过socket请求http
    url = urlparse(url)
    host = url.netloc
    path = url.path
    
    if path == "":
        path = '/'

    # 建立连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False) # 使用非阻塞IO，但是下面需要用while循环不停的检查状态
    try:
        client.connect((host, 80))
    except BlockingIOError:
        pass

    # 不停的询问连接是否建立好，需要while循环不停的去检查状态
    # 做计算任务或者再次发起其他的连接请求
    while True:
        try:
            client.send("GET {} HTTP/1.1\r\n Host:{}\r\nConnection:close\r\n\r\n".format(path,host).encode('utf8'))
            break
        except OSError:
            pass

    
    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError:
            continue
        if d:
            data += d
        else:
            break
    data = data.decode("utf-8")
    headers = data.split('\r\n\r\n')[0]
    html = data.split('\r\n\r\n')[1]
    print(headers)
    print(html)
    client.close()

if __name__ == '__main__':
    get_url('http://www.baidu.com')
