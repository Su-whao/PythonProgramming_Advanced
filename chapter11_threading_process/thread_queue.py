import threading
import time
from chapter11_threading_process import variables

def get_detail_html(detail_url_list):
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            # 使用另一个py文件中的变量（将变量存在另一个py文件中）
            # url = variables.detali_url_list.pop()
            print("get detail html started: {}".format(url))
            time.sleep(2)
            print("get detail html end")

def get_detail_url(detail_url_list):
    print("get detail url started")
    loop = 0
    while True:
        time.sleep(3)
        for i in range(20):
            detail_url_list.append("http://www.selfweb.com/{id}".format(id=i+loop*20))
        print("get detail url end")
        loop+=1

# 1 线程通信方式
## 通过全局变量
    
if __name__ == "__main__":
    detail_url_list = []
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_list,))
        html_thread.start()
    thread_detail_url.start()
