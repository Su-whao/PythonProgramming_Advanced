# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-10 13:28:14
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-10 13:48:50
 * @Description: None
'''

# 1. python中函数的工作原理

import inspect

frame = None

def foo():
    bar()

def bar():
    global frame
    frame = inspect.currentframe()

# python.exe 会用一个叫做 PyEval_EvalFramEx(c函数)去执行foo函数
# 首先会创建一栈帧

# python一切皆对象，栈帧也是对象，把代码转成字节码对象
# 在栈帧对象的上下文里面运行字节码对象

# 当foo调用子函数bar，又会创建一个栈帧，将函数的控制权交给bar的字节码
# 所有栈帧都是分配在堆内存上，这就决定了栈帧可以独立于调用者存在
# 在函数调用函数的形式当中，栈帧是类似递归的存在，可以从一层返回上一层


# import dis 
# print(dis.dis(foo)) # 查看字节码

foo()
print(frame.f_code.co_name)
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)

def gen_func():
    yield 1
    name = 'wanghao'
    yield 2
    age = 18
    return 'imooc'

import dis
gen = gen_func()
print(dis.dis(gen))

print(gen.gi_frame.f_lasti) # 当前执行到字节码的哪一行
print(gen.gi_frame.f_locals)    # 当前的局部变量

next(gen)
print(gen.gi_frame.f_lasti) # 当前执行到字节码的哪一行
print(gen.gi_frame.f_locals)    # 当前的局部变量

next(gen)
print(gen.gi_frame.f_lasti) # 当前执行到字节码的哪一行
print(gen.gi_frame.f_locals)    # 当前的局部变量
