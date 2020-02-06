
# 对象的类型取决于实现的魔法函数

class Cat(object):
    def say(self):
        print('I am a cat')


class Dog(object):
    def say(self):
        print("I am a dog")


class Duck(object):
    def say(self):
        print('I ma a duck')

animal_list = [Cat, Dog, Duck]
# 每个类都实现了 say 方法，因此每个类都可以调用 say，像魔法函数一样
# 魔法函数可以被python内置的函数操作也是根据每个内置函数都是对类中相同的魔法函数进行操作
for animal in animal_list:
    animal().say()


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

company = Company(['Tom', 'Bob', 'Jone'])

a = ['a', 'b']
# list.extend() 接收的参数是 iterable 可迭代对象，因此自己定义的，实现__getitem__方法的类也可以
# set tuple list 都可以
a.extend(company)
print(a)
