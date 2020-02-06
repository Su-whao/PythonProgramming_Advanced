# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-09 16:05:58
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-09 16:21:21
 * @Description: None
'''

from datetime import date, datetime

class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0
        
    def get_age(self):
        return datetime.now().year - self.birthday.year
    
    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value

if __name__ == '__main__':
    user = User('wanghao', date(year=1997, month=1,day=9))
    user.age = 30
    print(user._age)
    print(user.age)