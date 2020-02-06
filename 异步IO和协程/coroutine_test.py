# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-11 19:21:26
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-11 20:07:31
 * @Description: None
'''


# 1. 回调模式编码复杂度高
# 2. 同步编程的并发行不高
# 3. 多线程编程需要线程间同步，lock

# 1. 采用同步到的翻噶似编写异步的代码
# 2. 使用单线程去切换任务
#   1. 线程我是有操作系统切换的，单线程切换意味着我们需要程序员去自己调度任务
#   2. 不需要锁，并发行高，如果单线程内切换函数，性能远高于线程切换，并发行更高

# 传统函数调用过程 A->B->C 
# 我们需要一个可以暂停的函数，并且在适当的时候继续执行
# 出现了协程 -> 有多个入口

def gen_func():
    html = yield "http://www.baidu.com"
    print(html)
    return 

if __name__ == '__main__':
    gen = gen_func()
    import dis

    print(dis.dis(gen))
    # 在调用send发送非None值之前，我们必须启动一次生成器
    # 方式有两种，gen.send(), next(gen)
    url = gen.send(None)
    print(gen.gi_frame.f_lasti)
    # print(url)
    #download page
    html = 'WangHao'
    gen.send(html)
    print(gen.gi_frame.f_lasti)
    
    