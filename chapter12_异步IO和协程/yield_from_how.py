# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-12 09:47:40
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-12 10:07:08
 * @Description: None
'''


'''
总结：

1. 子生成器生产的值，都是直接传给调用方：调用方通过.send()发送的值都是直接传给子生成器的，如果发送的是None，会调用子生成器的__next__()方法，如果不是None，调用子生成器的send()方法。
2. 子生成器退出的时候，最后的return EXPR，会触发一个StopIteration(EXPR)异常；
3. yield from表达式的值，是子生成器终止时，传递给StopIteration异常的第一个参数；
4. 如果调用的时候出现StopIteration异常，委托生成器也会恢复运行，同时其他的异常会向上冒泡；
5. 传入委托生成器的异常里，除了GeneratorExit之外，其他的所有异常全都传递给子生成器的throw()方法，如果调用throw的时候出现了StopIteration异常，那么就恢复委托生成器的运行，其他的异常全部向上冒泡；
6. 如果在委托生成器上调用close()或传入GeneratorExit异常，会调用子生成器的close()方法，没有的话不调用，如果在调用的时候出现异常那么就向上冒泡，否则的话委托生成器会抛出GeneratorExit异常。
'''