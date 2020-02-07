# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-12 16:27:11
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-12 16:46:19
 * @Description: None
'''
# 1. run_until_complete

# import asyncio
# loop = asyncio.get_event_loop()
# loop.run_forever()  # 不停止一直运行
# loop.run_until_complete()   # 运行完停止


# 1. loop会被放到future种
# 2. 取消future

# import asyncio
# import time

# async def get_html(sleep_times):
#     print("waiting")
#     await asyncio.sleep(sleep_times)
#     print("done after {}s".format(sleep_times))

# if __name__ == '__main__':
#     task1 = get_html(2)
#     task2 = get_html(3)
#     task3 = get_html(4)

#     tasks = [task1, task2, task3]

#     loop = asyncio.get_event_loop()

#     try:
#         loop.run_until_complete(asyncio.wait(tasks))
#     except KeyboardInterrupt as e:
#         all_tasks = asyncio.Task.all_tasks()
#         for task in all_tasks:
#             print("cancel task")
#             print(task.cancel())
#         loop.stop()
#         loop.run_forever()
#     finally:
#         loop.close()


# 协程里面嵌套协程

import asyncio

async def compute(x, y):
    print("Compute %s + %s ..."%(x,y))
    await asyncio.sleep(1)
    return x+y

async def print_sum(x, y):
    result = await compute(x, y)
    print('%s + %s = %s' % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1,2))
loop.close() 