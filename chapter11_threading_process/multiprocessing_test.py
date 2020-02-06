import os
import time

# # fork 只能用于linux下
# pid = os.fork() # 创建一个子进程
# print("bob")
# if pid == 0:
#     print("子进程 {}， 父进程是：{}".format(os.getpid(), os.getppid()))
# else:
#     print("我是父进程 {}".format(pid))

# time.sleep(2)

from concurrent.futures import ProcessPoolExecutor
import multiprocessing

# 多进程编程
import time
def get_html(n):
    time.sleep(n)
    print("sub_process success")
    return n



if __name__ == "__main__":
    # process = multiprocessing.Process(target=get_html, args=(2,))
    # print(process.pid)
    # process.start()
    # print(process.pid)
    # process.join()
    # print("main process end")

    # 进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, args=(3,))

    # # 等待所有任务完成
    # pool.close()
    # pool.join()
    # print(result.get())

    # imap,打印顺序和添加顺序一样
    # for result in pool.imap(get_html, [1,5,3]):
    #     print("{} sleep success".format(result))

    # 执行顺序和添加顺序无关，谁先完成先打印谁
    for result in pool.imap_unordered(get_html, [1,4,3]):
        print("{} sleep success".format(result))