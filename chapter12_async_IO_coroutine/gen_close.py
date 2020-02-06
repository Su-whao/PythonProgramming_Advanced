# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-11 20:09:04
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-11 20:14:44
 * @Description: Noner
'''
def gen_func():
    html = yield "wanghao"
    print(html)
    yield 1
    yield 2
    yield 3
    return 'hahaha'



if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.close()
    print('wanghao')