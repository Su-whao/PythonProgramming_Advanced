# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-13 09:15:53
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-13 09:44:07
 * @Description: None
'''
# asyncio 没有提供http协议的接口 可以使用 aiohttp

import asyncio 

import socket
from urllib.parse import urlparse


async def get_url(url):
    # 通过socket请求http
    url = urlparse(url)
    host = url.netloc
    path = url.path
    port = 80
    
    if path == "":
        path = '/'

    # 建立连接
    reader, writer = await asyncio.open_connection(host, port) 

    writer.write("GET {} HTTP/1.1\r\n Host:{}\r\nConnection:close\r\n\r\n".format(path,host).encode('utf8'))

    all_lines = []
    # 异步for循环
    async for raw_line in reader:
        data = raw_line.decode("utf-8")
        all_lines.append(data)
    html = "\n".join(all_lines)
    return html

async def main(loop):
    tasks = [] 
    for url in range(20):
        url = "http://www.baidu.com"
        # 将get_url协程转为future，这样可以在外面拿到协程的执行结果
        tasks.append(asyncio.ensure_future(get_url(url)))
    
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result[:15])
    

if __name__ == "__main__":
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))

    print(time.time() - start_time)