# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-12 22:54:47
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-13 00:21:57
 * @Description: None
'''
import asyncio

def callback(sleep_times):
    print("sleep {} success".format(sleep_times))

def stoploop(loop):
    loop.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # loop.call_soon(callback, 2)
    # loop.call_soon(stoploop, loop)

    # call_later在指定时间后运行，跟传入的顺序无关
    # 这里的时间是loop内部的时间
    # loop.call_later(2, callback, 2)
    # loop.call_later(1, callback, 1)
    # loop.call_later(3, callback, 3)
    # loop.call_soon(callback, 4) # 最先执行

    # call_at
    now = loop.time()
    loop.call_at(now+2, callback, 2)
    loop.call_at(now+1, callback, 1)
    loop.call_at(now+3, callback, 3)
    loop.run_forever()

    # call_threadsaft 是线程安全的方法