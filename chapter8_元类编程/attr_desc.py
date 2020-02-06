# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-09 16:42:17
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-09 23:24:01
 * @Description: None
'''


from datetime import date, datetime
import numbers

class IntField:
    # 实现一下三个方法中的任何一个，可以将当前类作为属性描述符
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        '''
            :instance 是被描述的对象实例
            :value 是设置的值

            可以在这里进行设置的验证
        '''
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        self.value = value   

    def __delete__(self, instance):
        pass

class NonDataIntField:
    # 非数据属性描述符
    def __get__(self, instance, owner):
        return self.value


class Model:
    age = IntField()
    num = 1 # 不进入 __dict__
    def __init__(self):
        self.name = 'w' # 进入__dict__


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthady = birthday
        self._age = 0

    @property
    def age(self):
        return datetime.now() - self.birthday.year

    @age.setter
    def age(self, value):
        # 检查是否时字符串类型
        self._age = value


if __name__ == '__main__':
    #user = User('wanghao', date(year=1997, month=9, day=29))
    model = Model()
    model.age = 11 # 此时实际上是赋值到IntField的实例中
    print(model.age) # 此时也实际上是从IntField的实例中读 __get__ 方法来得到值
    print(model.num)
    print(model.__dict__)
