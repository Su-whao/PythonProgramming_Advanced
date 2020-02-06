# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-09 16:22:01
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-09 16:32:57
 * @Description: None
'''

# __getattr__ 就是在查找不到属性的时候调用

from datetime import date, datetime

class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    # 查找不到属性时进入这个函数，如果能查找到属性不进入这个函数
    # 可以用来返回这个类中的 info 属性
    def __getattr__(self, item):
        print('attr')
        return self.info[item]

    def __getattribute__(self, item):
        print('attributeS')

if __name__ == '__main__':
    user = User('wanghao', date(year=1997, month=1, day=9), info={'commany_name': 'imooc'})
    print(user.commany_name)