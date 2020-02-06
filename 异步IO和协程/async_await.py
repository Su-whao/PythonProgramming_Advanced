# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-12 10:48:21
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-12 10:53:37
 * @Description: None
'''
#python3.5 以后支持了原生的协程 async await

async def downloader(url):
    # 在async函数种不能使用yield
    return 'wanghao'

async def download_url(url):
    #do
    html = await downloader(url)
    return html


if __name__ == '__main__':
    coro = download_url('http://www.baidu.com')
    # 这里不能使用next() 而要使用send(None)
    coro.send(None)