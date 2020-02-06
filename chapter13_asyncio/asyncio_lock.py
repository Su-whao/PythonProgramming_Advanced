# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-13 09:51:55
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-13 10:02:03
 * @Description: None
'''

## 不需要锁
# total = 0

# async def add():
#     global  total
#     for i in range(1000000):
#         total += 1


# async def desc():
#     global total
#     for i in range(1000000):
#         total -= 1

    
# if __name__ == "__main__":
#     import asyncio
#     tasks = [add(), desc()]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))


import asyncio
from asyncio import Lock

lock = Lock()

cache = {}

async def get_stuff(url):
    # await lock.acquire()
    async with lock:    # 协程上下文
        if url in cache:
            return cache[url]

        stuff = await aiohttp.request('GET', url)
        cache[url] = stuff 
        return stuff
    # lock.release()

async def parse_stuff():
    stuff = await get_stuff()


async def use_stuff():
    stuff = await get_stuff()
