# -*- coding: utf-8 -*-
'''
 * @Author: WangHao
 * @Date: 2020-01-09 23:32:49
 * @LastEditors: WangHao
 * @LastEditTime: 2020-01-09 23:57:57
 * @Description: None
'''
# 类也是对象，type创建类的类

def  create_class(name):
    if  name == 'user':
        class User:
            def __str__(self):
                return 'user'
        return User
    elif name == 'company':
        class Company:
            def __str__(self):
                return 'company'
        return Company

class BaseClass:
    def answer(self):
        return 'I am baseclass'

# 传给type创建类的参数
def say(self):
    return 'I am user'



# 什么是元类？元类是创建类的类
# type是元类

class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        # 这里需要将 agrs kwagrs 参数传进去
        # 这里可以控制user的创建过程
        return super().__new__(cls, *args, **kwargs)

class User(metaclass=MetaClass):
    pass

# Python中类的实例化过程
# 首先寻找metaclass，通过metaclass来创建类，如果本身没有metaclass，那么会找父类的metaclass，如果实在找不到会调用type

if __name__ == '__main__':
    # MyClass = create_class('user')
    # my_obj = MyClass()
    # print(my_obj)

    # type
    # 用来获取对象类型，可以用来创建类
    # type动态创建类
    User = type('User', (BaseClass,), {'name': 'wanghao', 'say':say}) # 类名、基类、属性
    my_obj = User()
    print(my_obj.name)
    print(my_obj.__dict__)  # name没进入__dict__
    print(my_obj.answer())