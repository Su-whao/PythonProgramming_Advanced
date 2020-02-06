# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-13 00:22:28
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-13 00:44:21
 * @Description: None
'''
# 使用短线成：在协程中集成阻塞IO

import asyncio

from concurrent.futures import ThreadPoolExecutor
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
    print(data)
    client.close()


if __name__ == "__main__":
    import time
    startTime = time.time()
    
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    tasks = []
    for url in range(20):
        url = "http://www.baidu.com"
        task = loop.run_in_executor(executor, get_url, url)
        tasks.append(task)
    # 速度好快啊，只有零点几秒
    loop.run_until_complete(asyncio.wait(tasks))
    print("last time: {}".format(time.time()-startTime))

