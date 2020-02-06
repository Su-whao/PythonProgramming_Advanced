from threading import Condition
import threading
# 条件变量，用于复杂的线程间同步

# 通过Condition完成读诗
class Xiaoai(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        # condition可以使用with语句，也可以使用成对的acquire和release方法。
        # self.cond.acquire()
        with self.cond:
            self.cond.wait()
            print("{} : 在".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 好".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 曲项向天歌".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 红掌拨清波".format(self.name))
            self.cond.notify()

        # self.cond.release()

class Tianmao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        self.cond.acquire()
            
        print("{} : 小爱同学".format(self.name))
        self.cond.notify()
        
        self.cond.wait()
        print("{} : 我们来对古诗吧".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{} : 鹅鹅鹅".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{} : 白毛浮绿水".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{} : 好！！！".format(self.name))
        self.cond.notify()

        self.cond.release()

# 启动顺序很重要
# 在调用wait之前要先 acquire，with语句帮助实现了这一步
# condition有两层锁，一把底层锁会在线程调用了wait 的时候释放，上面的锁会在每次调用wait的时候分配一把并放入到cond的等待队列中，等待notify方法的唤醒。
if __name__ == "__main__":
    cond = threading.Condition()
    xiaoai = Xiaoai(cond)
    tianmao = Tianmao(cond)
    # 虽然是天猫先说话，但是要先启动小爱，让小爱在wait等待天猫的通知。
    # 否则会阻塞
    xiaoai.start()
    tianmao.start()