# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-11 10:14:08
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-11 15:10:38
 * @Description: None
'''
import socket
from urllib.parse import urlparse
from selectors import  DefaultSelector, EVENT_READ, EVENT_WRITE

# 使用select完成http请求

# select + 回调 + 事件循环

# 好处，并发性高

selector = DefaultSelector()
urls = ["http://www.baidu.com"]
stop = False

class Fetcher:
    def get_url(self, url):
        # 通过socket请求http
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        
        if self.path == "":
            self.path = '/'
        self.data = b''

        # 建立连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False) # 使用非阻塞IO，但是下面需要用while循环不停的检查状态

        try:
            self.client.connect((self.host, 80))
        except BlockingIOError:
            pass
        

        ## 注册selector 回调
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)

    # 回调
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\n Host:{}\r\nConnection:close\r\n\r\n".format(self.path,self.host).encode('utf8'))
        # 注册回调
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    # 回调
    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf-8")
            print(data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True
        

# 事件循环，不停的请求socket的状态并调用对应的回调函数
def loop():
    # select 本身是不支持register模式的
    # 这里的selector是封装好的select
    # select状态变化以后的回调是由程序员来完成的
    # 回调+事件循环+select（poll、epoll）
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)



if __name__ == '__main__':
    fetcher = Fetcher()
    fetcher.get_url("http://www.baidu.com")
    loop()


# def get_url(url):
#     # 通过socket请求http
#     url = urlparse(url)
#     host = url.netloc
#     path = url.path
    
#     if path == "":
#         path = '/'

#     # 建立连接
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.setblocking(False) # 使用非阻塞IO，但是下面需要用while循环不停的检查状态
#     try:
#         client.connect((host, 80))
#     except BlockingIOError:
#         pass

#     # 不停的询问连接是否建立好，需要while循环不停的去检查状态
#     # 做计算任务或者再次发起其他的连接请求
#     while True:
#         try:
#             client.send("GET {} HTTP/1.1\r\n Host:{}\r\nConnection:close\r\n\r\n".format(path,host).encode('utf8'))
#             break
#         except OSError:
#             pass

    
#     data = b""
#     while True:
#         try:
#             d = client.recv(1024)
#         except BlockingIOError:
#             continue
#         if d:
#             data += d
#         else:
#             break
#     data = data.decode("utf-8")
#     headers = data.split('\r\n\r\n')[0]
#     html = data.split('\r\n\r\n')[1]
#     print(headers)
#     print(html)
#     client.close()
