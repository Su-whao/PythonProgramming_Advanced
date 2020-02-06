# 通过queue方式进行线程间同步
import time
import threading
from queue import Queue

def get_detail_html(queue):
    while True:
        url = queue.get() # 阻塞方法，Qeueue是线程安全
        print("get detail html started: {}".format(url))
        time.sleep(2)
        print("get detail html end")

def get_detail_url(queue):
    print("get detail url started")
    loop = 0
    while True:
        time.sleep(3)
        for i in range(20):
            queue.put("http://www.selfweb.com/{id}".format(id=i+loop*20))
        print("get detail url end")
        loop+=1

# 2 线程通信方式
## 通过Queue
    
if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_list,))
        html_thread.start()
    thread_detail_url.start()
