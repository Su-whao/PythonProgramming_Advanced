# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-10 12:48:51
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-10 13:52:18
 * @Description: None
'''

from collections.abc import Iterator


# 在创建可迭代对象的时候，通过 iter 函数返回一个迭代器，在迭代器里面实现 next 方法，而不是在本身类里面实现和维护next
class Company(object):
    def __init__(self, employee_list):
        self.employee_list = employee_list

    # iter 和 getitem 方法得区别时什么？
    # 先找iter，找不到会去找getitem
    # 可以被 iter() 方法操作
    def __iter__(self):
        return MyIterator(self.employee_list)

    # def __getitem__(self, item):
    #     return self.employee_list[item]


# 实现一个迭代器
class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0
        
    def __next__(self):
        # 真正返回迭代值得逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == '__main__':
    company = Company(['tom', 'andy', 'bob'])
    # for 循环会取调用 __iter__ 函数
    # 虽然类没有实现 iter ，但是 getitem 回去判断是否定义 iter ，没有则会创建一个默认的迭代器，利用  getitem 函数进行遍历（从0开始）
    my_itor = iter(company)
    for i in my_itor:
        print(i)
    for item in company:
        print(item)
    print(company)
    print(my_itor)

    # for循环内部操作
    # while True:
    #     try:
    #         next(my_itor)
    #     except StopIteration as e:
    #         pass
