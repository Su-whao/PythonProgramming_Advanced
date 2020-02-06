# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-10 13:12:54
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-10 13:26:07
 * @Description: None
'''

# 生成器函数，函数里只有要 yield 关键词就是生成器函数，不再是一个普通函数。
# 生成器函数，返回的是一个生成器对象
# 生成器对象也实现了迭代器协议
def gen_func():
    yield 1


# 斐波那契数列
def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index-1)+fib(index-2)

def fib2(index):
    re_list = []
    n,a,b = 0,0,1
    while n<index:
        re_list.append(b)
        a,b=b,a+b
        n+=1
    return re_list

def gen_fib(index):
    n,a,b = 0,0,1
    while n<index:
        yield b
        a,b = b,a+b
        n += 1
    

if __name__ == '__main__':
    # 生成器对象，在python编译字节码的时候产生。
    gen = gen_func()

    for data in gen_fib(10):
        print(data)