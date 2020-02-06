# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-10 21:42:12
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-11 09:25:04
 * @Description: None
'''

import socket
from urllib.parse import urlparse

def get_url(url):
    # 通过socket请求http
    url = urlparse(url)
    host = url.netloc
    path = url.path
    
    if path == "":
        path = '/'

    # 建立连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.setblocking(False) # 使用非阻塞IO，但是下面需要用while循环不停的检查状态
    client.connect((host, 80))

    client.send("GET {} HTTP/1.1\r\n Host:{}\r\nConnection:close\r\n\r\n".format(path,host).encode('utf8'))
    
    data = b""
    while True:
        d = client.recv(1024)
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

