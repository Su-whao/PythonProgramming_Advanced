# 不建议继承list和dict

class Mydict(dict):
    def __setitem__(self, k, v):
        super().__setitem__(k, v*2)

my_dict = Mydict(one=1)
print(my_dict)  # 1
# 默认的dict是用C语言写的，有些情况下不会执行这些魔法函数
my_dict['one'] = 1
print(my_dict)  # 2

from collections import UserDict

class Mydict2(UserDict):
    def __setitem__(self, k, v):
        super().__setitem__(k, v*2)

my_dict = Mydict2(one=1)
print(my_dict)  # 2
# 默认的dict是用C语言写的，有些情况下不会执行这些魔法函数
my_dict['one'] = 1
print(my_dict)  # 2


from collections import defaultdict

my_dict = defaultdict(int)
my_value = my_dict['one']
pass 