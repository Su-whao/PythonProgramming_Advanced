# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-11 21:22:37
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-12 09:42:01
 * @Description: None
'''

# 如果最后一个send之后没有yield，那么最后一个send会报StopIteration错误
# 如下写成两层的生成器结构，内层一个while循环，外层一个while循环，不会报StopIteration错误

def gen_func():
    total = []
    while True:
        x = yield
        if not x :
            break
        total.append(x)
    return total

def gen_func2():
    # 这里用while True不会报StopIteraton此错误，如果不使用while True则需要捕获异常
    while True:
        r = yield from gen_func()
        print('OK2', r)

gen = gen_func2()


gen.send(None)
gen.send('a')
gen.send('b')
gen.send(None)

# def gen_func2():
#     yield 1
#     yield 2
#     yield 3

# gen = gen_func2()
# print(gen)
# # print(gen.__next__())
# # print(gen.__next__())
# # print(gen.__next__())
# print(gen.send(None))
# print(gen.send(None))
# print(gen.send(None))