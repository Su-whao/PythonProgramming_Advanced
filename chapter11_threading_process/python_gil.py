# gil: global interpreter lock: 全局解释器锁
# python 中一个线程对应于C语言的一个线程
# gil 使得同一时刻只有一个线程运行在一个CPU上执行字节码，无法将多个线程映射到多个CPU上，无法利用多核优势。
# gil 会根据执行的字节码行数以及时间片释放gil，gil 会在遇到IO操作时主动释放。

import dis
def add(a):
    a = a+1
    return a

print(dis.dis(add))



total = 0
def add():
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)