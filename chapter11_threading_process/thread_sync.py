from threading import Lock
from threading import RLock # 可重入的锁

# 在同一个线程里面可以调用多次acquire，一定注意acquire的次数和release次数相等

total = 0
lock = RLock()

def add():
    '''
    1. load a
    2. load 1
    3. +
    4. 赋值给a
    '''
    global lock
    global total
    for _ in range(1000000):
        lock.acquire()
        total += 1
        dosomething(lock)
        lock.release()

def dosomething(lock):
    lock.acquire() # 此处是该线程连续第二个acquire，使用Lock会死锁，可使用RLock
    #do something
    lock.release()
def desc():
    '''
    1. load a
    2. load 1
    3. -
    4. 赋值给a
    '''
    global lock
    global total
    for _ in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


# 1. 锁会影响性能
# 2. 锁会引起死锁
'''
A(a,b)
acquire (a)
acquire (b)

B(b,a)
acquire (b)
acquire (a)

A 需要a和b，B 需要b和a，会造成死锁
'''
if __name__ == '__main__':

    # import dis
    # print(dis.dis(add))
    # print(dis.dis(desc))

    import threading
    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(total)  # 一直为 0， 因为两个线程加了锁，一直交替运行。