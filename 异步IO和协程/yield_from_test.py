# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-11 20:19:46
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-11 20:23:55
 * @Description: None
'''
from itertools import chain

my_list = [1,2,3]
my_dist = {
    'w1': 'www.baidu.com',
    'w2': 'www.toutiao.com'
}

def my_chain(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable
        # for value in my_iterable:
        #     yield value


for value in my_chain(my_list, my_dist, range(5, 10)):
    print(value)