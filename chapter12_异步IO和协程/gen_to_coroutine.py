# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-12 10:36:53
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-12 10:40:17
 * @Description: None
'''

import inspect


# 1. 用同步的方式编写异步代码，

def gen_func():
    yield 1 
    return 2

if __name__ == '__main__':
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen))
