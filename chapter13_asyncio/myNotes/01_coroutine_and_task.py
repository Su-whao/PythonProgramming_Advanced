##
## 协程
##

# 协程通过 async/await 语法进行声明，是编写异步应用的推荐方式。例如，以下代码段 (需要 Python 3.7+) 打印 "hello"，等待 1 秒，然后打印 "world":

import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("world")

# asyncio.run(main()) # 成功执行
# main()    # 直接调用不能执行

# 运行协程三种机制
# 1. asyncio.run()  运行最高层级的入口点 main() 函数

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    # 串行的
    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())
'''
输出：
started at 15:47:50
hello
world
finished at 15:47:53
# 总花费时间 3 秒
'''


# 2. asyncio.create_task() 函数用来并发运行作为 asyncio 任务的多个协程
async def main():
    # 创建两个协程
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    # 并行运行的
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())
'''
输出：
started at 15:51:17
hello
world
finished at 15:51:19
# 总花费时间 2 秒
这种方式是并行的，比上一种代码运行快1秒。
'''

##
## 可等待对象
##

# 如果一个对象可以在 await 语句中使用，那么他就是可等待的的对象，
# 可等待对象有三种主要类型：协程、任务、Future

## 协程
import asyncio 

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()"
    # A coroutine object is created but not awaited
    # so it won't tun at all
    nested()
    # 此处直接调用 nested() 会抛出一个异常：RuntimeWarning: coroutine 'nested' was never awaited nested()
    # 但是程序不会停止，会继续往下执行

    print(await nested())   # 正常打印42

# asyncio.run(main())

## 任务
# 任务被用来设置日程以便并发执行协程
# 当一个协程通过 asyncio.create_task() 等函数被打包成为一个任务，该协程将自动排入日程准备立即运行

import asyncio

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()"
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simple be awaitde to wait until it is complete

    # result = task.cancel() 
    # 执行成功后哦，task.canceled()不回返回True
    # 执行成功后，在 await task 会抛出 CancelledError 错误
    # print(result)
    # isCancel = task.cancelled() # 返回是否被取消
    # print(isCancel)
    result = await task
    print(result)

# asyncio.run(main())


##
## 休眠
##

import asyncio
import datetime

async def display_date():
    '''
    运行5秒，每秒打印一次时间
    '''
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

# asyncio.run(display_date())


##
##  并发运行任务
##

# awaitable asyncio.gather(*aws, loop=None, return_exceptions=False)
#   1. 并发运行aws序列中的可等待对象
#   2. 如果aws中某个可等待对象为协程，他将自动作为一个任务加入日程
#   3. 如果所有可等待对象都成功完成，结果将是一个由所有返回值聚合成的列表，结果值的顺序与aws中可等待对象的顺序一致
#   4. 如果 return_exceptions 为 False(默认)，所引发的首个异常会立即传播给等待 gather() 的任务。aws序列中的其他可等待对象不会被取消并将继续运行
#   5. 如果 return_exceptions 为 True，异常会和成功的结果一样处理，并聚合至结果列表。
#   6. 如果 gather() 被取消，所有被提交 (尚未完成) 的可等待对象也会 被取消。
#   7. 如果 aws 序列中的任一 Task 或 Future 对象 被取消，它将被当作引发了 CancelledError 一样处理 -- 在此情况下 gather() 调用 不会 被取消。这是为了防止一个已提交的 Task/Future 被取消导致其他 Tasks/Future 也被取消。
import asyncio
import time
async def factorial(name,  number):
    f = 1
    for  i in range(2, number+1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    start_time = time.time()
    # Schedule three calls *concurrently*:
    result = await asyncio.gather(
        factorial('A', 2),
        factorial("B", 4),
        factorial("C", 6),
        return_exceptions=True
    )
    # 返回的结果顺序与 gather() 参数顺序一致
    print(f"Result is: {result}")
    print(f"Total time: {round(time.time() - start_time,1)}s")
    # 共花费5秒

async def main2():
    # submit task to gather
    # Create tasks
    task1 = asyncio.create_task(factorial('A', 2))
    task2 = asyncio.create_task(factorial('B', 3))
    task3 = asyncio.create_task(factorial("C", 4))

    task3.cancel()
    # result = await asyncio.gather(task1, task2, task3)  # task3 被取消，执行到task3 时立即抛出CancelledError错误
    result = await asyncio.gather(task1, task2, task3, return_exceptions=True) # task3 被取消，但是 gather() 正常执行，返回结果中 task3 的位置是一个 CancelledError 错误对象
    # task3.cancel() # 没有起作用
    print(f"Gather Result: {result}")

# asyncio.run(main2())

##
## wait
##

# coroutine asyncio.wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED)
# aws 参数是一个序列，set list tuple
## return_when 参数：
##   FIRST_COMPLETED  函数将在任意可等待对象结束或取消时返回。
##   FIRST_EXCEPTION  函数将在任意可等待对象因引发异常而结束时返回。当没有引发任何异常时它就相当于 ALL_COMPLETED。
##   ALL_COMPLETED    函数将在所有可等待对象结束或取消时返回。
# 并发运行 aws 指定的 可等待对象 并阻塞线程直到满足 return_when 指定的条件。
# 如果 aws 中的某个可等待对象为协程，它将自动作为任务加入日程。直接向 wait() 传入协程对象已弃用，因为这会导致 令人迷惑的行为。
# 返回两个 Task/Future 集合: (done, pending)。

async def main3():
    # Create tasks
    task1 = asyncio.create_task(factorial('A', 2))
    task2 = asyncio.create_task(factorial('B', 3))
    task3 = asyncio.create_task(factorial("C", 4))
    done, pending = await asyncio.wait([task1, task2, task3])
    # done： 返回时已完成线程
    # pending： 返回时未完成县城额
    print(done, pending)

# asyncio.run(main3())

# asyncio.as_completed(aws, *, loop=None, timeout=None)¶
# 并发地运行 aws 集合中的 可等待对象。返回一个 Future 对象的迭代器。返回的每个 Future 对象代表来自剩余可等待对象集合的最早结果。
# 如果在所有 Future 对象完成前发生超时则将引发 asyncio.TimeoutError。

async def main4():
    # Create tasks
    task1 = asyncio.create_task(factorial('A', 2))
    task2 = asyncio.create_task(factorial('B', 3))
    task3 = asyncio.create_task(factorial("C", 4))

    for f in asyncio.as_completed((task1, task2, task3)):
        # 一个协程执行完立即返回结果，并执行下面的语句
        result = await f
        print(result)
asyncio.run(main4())
