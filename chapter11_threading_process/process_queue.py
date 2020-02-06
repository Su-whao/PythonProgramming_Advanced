from multiprocessing import Process, Queue, Pool, Manager, Pipe

import time

# def producer(queue):
#     queue.put("a")
#     time.sleep(2)

# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)


# # 共享全局变量在多进程中不适用，多进程中的数据是隔离的，两边互不影响
# if __name__ == "__main__":
#     queue = Queue(10)
#     my_producer = Process(target=producer, args=(queue,))
#     my_consumer = Process(target=consumer, args=(queue, ))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()

# multiprocessing 中的queue不能用于pool进程池

def producer(queue):
    queue.put("a")
    time.sleep(2)

def consumer(queue):
    # time.sleep(2)
    data = queue.get()
    print(data)


# 共享全局变量在多进程中不适用，多进程中的数据是隔离的，两边互不影响
# queue不能用于进程池中通信
# pool中的进程间通信要使用Manager中的Queue

# 三个 Queue
# from queue import Queue
# from multiprocessing import Queue
# from multiprocessing import Manager
# Manager().Queue
# if __name__ == "__main__":
#     # queue = Queue(10) # 没有打印 a
#     queue = Manager().Queue(10)
    
#     pool = Pool(2)
#     pool.apply_async(producer, args=(queue,))
#     pool.apply_async(consumer, args=(queue,))

#     pool.close()
#     pool.join()


# 通过Pipe实现进程间通信
# Pipe性能高于queue
# def producer(pipe):
#     pipe.send('wanghao')

# def consumer(pipe):
#     print(pipe.recv())

# if __name__ == "__main__":
#     recevie_Pipe, send_Pipe = Pipe()
#     # Pipe 只能适用于两个进程
#     my_producer = Process(target=producer, args=(send_Pipe,))
#     my_consumer = Process(target=consumer, args=(recevie_Pipe,))

#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()


# 多进程共享内存（变量）
def add_data(p_dict, key, value):
    p_dict[key] = value

if __name__ == "__main__":
    progress_dict = Manager().dict()

    first_process = Process(target=add_data, args=(progress_dict, "wanghao1", 1))
    second_process = Process(target=add_data, args=(progress_dict, "wanghao2", 2))

    first_process.start()
    second_process.start()
    first_process.join()
    second_process.join()
     
    print(progress_dict)