'''
class asyncio.Queue(maxsize=0,*,loop=None)
    当maxsize小于等于0，大小是无限的。当maxsize大于0，当队列到达maxsize时，await put() 将阻塞至某个元素被 get() 取出。
    不是线程安全的

class asyncio.PriorityQueue
    按优先级顺序去除（最小的先取出）
    条目时(priority_number, data)形式的元组

class asyncio.LifoQueue
    后进先出的队列（栈）

异常： asyncio.QueueEmpty, asyncio.QueueFull
'''

# 用队列实现多个并发任务的工作量分配
import asyncio
import random
import time

async def worker(name, queue):
    while True: # 一直从queue中获取元素
        # Get a "work item" out og the queue
        sleep_for = await queue.get()
        # sleep for the "sleep_for" second
        await asyncio.sleep(sleep_for)

        # notify the queue that the "work item" has been processed
        queue.task_done()

        print(f"{name} has slept for {sleep_for:.2f} seconds")

async def main():
    # Create a queue that we will use to store our "workload"
    queue = asyncio.Queue()

    # Generate random timings and put them into the queue.
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    # Create three worker tasks to process the queue concurrently.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f"worker-{i}", queue))
        tasks.append(task)

    # Wait until the queue is fully processed.
    started_at = time.monotonic()
    await queue.join()  # 阻塞直到queue中所有元素都done
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks.
    # queue中元素已经执行完，取消任务
    for task in tasks:
        task.cancel()

    # Wait until all worker tasks are cancelled.
    # result中都是CancelledError
    result = await asyncio.gather(*tasks, return_exceptions=True)

    print("===")
    print(f"3 workers slept in parallel for {total_slept_for:.2f} seconds")
    print(f"total expected sleep time: {total_sleep_time:.2f} seconds")
    print(result)

asyncio.run(main())