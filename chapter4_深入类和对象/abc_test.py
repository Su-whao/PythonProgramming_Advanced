

# 检查某个类是否有某个方法

class Company(object):
    name = 'keji'
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

# company = Company(['a', 'b', 'c'])
# # 检查类是否有某个方法
# print(hasattr(company, "__len__")) # True
# print(hasattr(company, "name")) # True
# print(hasattr(company, "employee")) # True

# # 我们在某些情况之下希望判定某个对象的类型
# from collections.abc import Sized
# print(isinstance(company, Sized)) # True

# 我们需要强制某个子类必须实现某些方法
# 例如实现了一个web框架，集成cache（redis， cache， memarycache）
# 需要设计一个抽象基类，指定子类必须实现某些方法


# 如何模拟一个抽象基类
class CacheBase():
    def get(self, key):
        raise NotImplementedError
    def set(self, key, value):
        raise NotImplementedError

class RedisCache(CacheBase):
    def say(self):
        print('This is redis cache.')

# redisCache = RedisCache()
# 子类没有实现get，set方法，只有在调用set方法的时候才会抛出异常，实例化是不会抛出异常
# redisCache.set('a', 1)

import abc
class CacheBase2(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass
    @abc.abstractmethod
    def set(self, key, value):
        pass

class RedisCache2(CacheBase2):
    pass

# 子类没有实现get set，在实例化时会报错
# redisCache2 = RedisCache2()

# 实现了一些抽象基类
import collections.abc

class A:
    pass

class B(A):
    pass

b = B()
print(isinstance(b, A)) # True