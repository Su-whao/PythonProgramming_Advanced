# 对于IO操作来说，多线程核多进程性能差别不大

# 通过Thread类实例化
import threading
import time
def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")

def get_detail_url(url):
    print("get detail url started")
    time.sleep(3)
    print("get detail url end")


class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
    def run(self):
        print("get detail url started")
        time.sleep(3)
        print("get detail url end")

    
if __name__ == "__main__":
    # thread1 = threading.Thread(target=get_detail_html, args=('',))
    # thread2 = threading.Thread(target=get_detail_url, args=('',))

    # # 设置主线程结束时关闭子线程（守护线程）
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)

    # start_time = time.time()
    # thread1.start()
    # thread2.start()

    # # 阻塞，等子线程执行完之后再往下执行
    # thread1.join()
    # thread2.join()

    # print("last time: {}".format(time.time()-start_time))

    
    ## 通过继承 Threading 来实现多线程
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")

    start_time = time.time()
    thread1.start()
    thread2.start()

    print("last time: {}".format(time.time()-start_time))
