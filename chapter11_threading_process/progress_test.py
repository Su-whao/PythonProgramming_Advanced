# 多进程编程
# 耗CPU的操作，用多进程
# 多进程可以利用多CPU优势
# 进程切换代价高于线程

# 1. 对于耗费CPU的操作，多进程优于多线程

from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
import time

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    with ProcessPoolExecutor(3) as executor: # 多进程（该计算任务，多进程比多线程快）
    # with ThreadPoolExecutor(3) as executor:   # 多线程
        all_task = [executor.submit(fib, (num)) for num in range(25,40)]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result {}".format(data))
        print("last time is {}".format(time.time()-start_time))


