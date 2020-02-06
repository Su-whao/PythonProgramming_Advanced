# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-12 11:23:29
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-12 16:26:21
 * @Description: None
'''
# 使用asyncio
import time
import asyncio

# async def get_html(url):
#     print('start get url')
#     # await 后面跟的必须是awaitable对象
#     time.sleep(2)
#     print('end get url')

# if __name__ == '__main__':
#     startTime = time.time()
#     loop = asyncio.get_event_loop() # 完成select操作
#     tasks  = [get_html('lalala') for i in range(5)]
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(time.time()-startTime)


## 获取协程的返回值
# from functools import partial
# async def get_html(url):
#     print('start get url')
#     # await 后面跟的必须是awaitable对象
#     # time.sleep(2)
#     return 'wanghao'

# def callback(url, future):
#     print(url)

# if __name__ == '__main__':
#     startTime = time.time()
#     loop = asyncio.get_event_loop() # 完成select操作
#     # get_future = asyncio.ensure_future(get_html('www'))
#     task = loop.create_task(get_html('www'))
#     # partial 可以将一个函数包装成另一个函数，这里用来给callback传参数
#     task.add_done_callback(partial(callback, "http://www.imooc.com"))
#     loop.run_until_complete(task)
#     print(task.result())


## wait 和 gather 区别


async def get_html(url):
    print('start get url')
    # await 后面跟的必须是awaitable对象
    await asyncio.sleep(2)
    print('end get url')

if __name__ == '__main__':
    startTime = time.time()
    loop = asyncio.get_event_loop() # 完成select操作
    # tasks  = [get_html('lalala') for i in range(5)]
    # loop.run_until_complete(asyncio.wait(tasks))
    # # loop.run_until_complete(asyncio.gather(*tasks))w
    # print(time.time()-startTime)

    #gather 和 wait 区别
    # gathwe更加high-level，可定制化更高
    task1 = [get_html("http://www.baidu.com") for i in range(10)]
    task2 = [get_html("http://www.imooc.com") for i in range(10)]

    # task1 = asyncio.gather(*task1)
    # task2 = asyncio.gather(*task2)
    # task2.cancel()   # 可取消任务(报错CancelledError)

    loop.run_until_complete(asyncio.gather(*task1, *task2))
    print(time.time()-startTime)